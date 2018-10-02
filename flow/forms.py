from django.forms import ModelForm
from .models import User


class SignupForm( ModelForm ):
    class Meta:
        model = User
        fields = [ 'username', 'email', 'password', 'first_name', 'last_name', 'profile_picture' ]
