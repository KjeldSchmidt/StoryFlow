from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Game
from django.utils import translation


def index( request ):
    translation.activate('de')
    return render( request, 'flow/index.html', {
        'user_name': 'carl'
    } )


def signup( request ):
    if request.method == 'POST':
        form = UserCreationForm( request.POST )
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get( 'username' )
            raw_password = form.cleaned_data.get( 'password1' )
            user = authenticate( username=username, password=raw_password )
            if user is not None:
                login( request, user )
            return redirect( 'home' )
    else:
        form = UserCreationForm()
    return render( request, 'flow/signup.html', {
        'form': form
    } )


def game( request, game_id ):
    try:
        game = Game.objects.get( pk=game_id )
    except Game.DoesNotExist:
        raise Http404( "Game does not exist" )
    return HttpResponse( str( game ) )
