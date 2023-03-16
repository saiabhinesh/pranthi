from django.shortcuts import render
from django.views import View  
from django.http import HttpResponse
from .forms import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from pranthi_app.custom_authentication import EmailPhoneUsernameAuthenticationBackend
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


class UserRegistration(APIView):
    form_class = RegistrationForm
    template_name = 'user_form.html'
    serializer_class = RegistrationSerializer
    def get(self,request,*args,**kwargs):
        try:
            return render(request,self.template_name,{'user_form':self.form_class})
        except Exception as e:
            return Response({"msg":"something went wrong in server"+str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self,request,*args,**kwargs):
        try:
            serializer_data =  self.serializer_class(data=request.POST)
            if serializer_data.is_valid():
                serializer_data.save()
                return render(request,'home.html',status=status.HTTP_200_OK)
            else:
                return Response({"msg":"error in validataion"+str(serializer_data.errors)},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            return Response({"msg":"something went wrong in server"+str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LoginView(APIView):
    form_class = LoginForm
    template_name = 'user_form.html'
    serializer_class =  LoginSerializer

    def get(self,request, *args, **kwargs):
        try:
            return render(request,self.template_name,{"user_form":self.form_class})
        except Exception as e:
            return Response({"msg":"something went wrong in server"+str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)        
    def post(self,request,*args,**kwargs):
        try:
            serializer_data =  self.serializer_class(data=request.POST)
            if serializer_data.is_valid():
                username = serializer_data.validated_data['username']
                password = serializer_data.validated_data['password']
                #note here we username means it can take both email and phone number the code is custom_authenticate method
                user = EmailPhoneUsernameAuthenticationBackend()
                user = user.custom_authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return render(request,'home.html',status=status.HTTP_200_OK)
                else:
                    messages.error(request, "Error. email or phone number is not valid")
                    return render(request,self.template_name,{"user_form":self.form_class})
            else:
                return Response({"msg":"error in validataion"+str(serializer_data.errors)},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except Exception as e:
            return Response({"msg":"something went wrong in server"+str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def LogOutView(request):
    logout(request)
    return HttpResponse("you are logged out")

