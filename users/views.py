from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def login_view( request ):
    username = request.POST[ 'username_storyflow' ]
    password = request.POST[ 'password_storyflow' ]
    user = authenticate( request, username=username, password=password )
    if user is not None:
        login( request, user )
        return redirect( 'index' )
    else:
        return redirect( 'index' )


def login_failed( request ):
    return redirect( 'index' )


def logout_view( request ):
    logout( request )
    return redirect( 'index' )
