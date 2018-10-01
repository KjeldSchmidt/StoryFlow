from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Game, User

admin.site.register( Game )
admin.site.register( User, UserAdmin )
