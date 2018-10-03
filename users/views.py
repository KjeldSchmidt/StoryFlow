from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect


def redirect_to_origin( request ):
    return HttpResponseRedirect( request.META.get( 'HTTP_REFERER', '/' ) )


def login_view( request ):
    username = request.POST[ 'username_storyflow' ]
    password = request.POST[ 'password_storyflow' ]
    user = authenticate( request, username=username, password=password )
    if user is not None:
        login( request, user )
        return redirect_to_origin( request )
    else:
        return redirect_to_origin( request )


def login_failed( request ):
    return redirect_to_origin( request )


def logout_view( request ):
    logout( request )
    return redirect_to_origin( request )
