from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Game


def index( request ):
    return render( request, 'flow/index.html' )


def signup( request ):
    if request.method == 'POST':
        form = UserCreationForm( request.POST )
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get( 'username' )
            raw_password = form.cleaned_data.get( 'password1' )
            user = authenticate( username=username, password=raw_password )
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
