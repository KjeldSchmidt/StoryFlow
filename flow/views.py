from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Game
from .forms import SignupForm


def index( request ):
    return render( request, 'flow/index.html', {
        'user_name': 'carl'
    } )


def signup( request ):
    if request.method == 'POST':
        form = SignupForm( request.POST )
        if form.is_valid():
            form.save()
            return redirect( 'index' )
    else:
        form = SignupForm()
    return render( request, 'flow/signup.html', {
        'form': form
    }   )


def game( request, game_id ):
    try:
        game = Game.objects.get( pk=game_id )
    except Game.DoesNotExist:
        raise Http404( "Game does not exist" )
    return HttpResponse( str( game ) )
