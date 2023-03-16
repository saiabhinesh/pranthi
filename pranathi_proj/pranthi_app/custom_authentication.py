from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()

class EmailPhoneUsernameAuthenticationBackend(object):
    @staticmethod
    def custom_authenticate(request, username=None, password=None):
        try:
            user = User.objects.get(
                Q(phone_no=username) | Q(email=username)
            )

        except User.DoesNotExist:
            return None

        if user and check_password(password, user.password):
            return user
        return None

    @staticmethod
    def get_user(user_id):
        
        try:
            return User.objects.get(pk=user_id)
        
        except User.DoesNotExist:
            return None