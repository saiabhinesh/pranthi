<h2>Task Key Points</h2>
<li>used custom model(CustomUser) inheriting from AbstractUser level, having phone number, email, UUID(primary key) and having index on phone number for quick results</li>
<li>used custom Authentication(EmailPhoneUsernameAuthenticationBackend) validates phone number (or)  email.
<li>used complete exception handlings, messages module for errors while rendering HTML, Exceptions messages for while rendering Json.
<li>Used Model form classes and Model serializers for complete validations, serialization as per requirement.
