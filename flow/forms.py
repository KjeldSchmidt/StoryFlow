from django.forms import ModelForm, Textarea, HiddenInput
from .models import User, Game


class SignupForm( ModelForm ):
    class Meta:
        model = User
        fields = [ 'username', 'email', 'password', 'first_name', 'last_name', 'profile_picture' ]


class GameCreationForm( ModelForm ):
    class Meta:
        model = Game
        fields = [ 'name', 'description', 'creator', 'first_story' ]
        widgets = {
            'description': Textarea( attrs={
                'cols': 60,
                'rows': 10
            } ),
            'creator': HiddenInput(),
            'first_story': HiddenInput(),
        }
        error_css_class = 'error'
