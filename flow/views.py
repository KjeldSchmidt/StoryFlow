from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Game
from .forms import SignupForm, GameCreationForm
from django.utils.translation import gettext as _
from .default_models import first_story_on_new_game


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
    } )


def create_game( request ):
    if not request.user.is_authenticated:
        return redirect( '/signup' )
    elif request.method == 'POST':
        game_form = GameCreationForm( request.POST )
        if game_form.is_valid():
            game = game_form.save()
            first_story = first_story_on_new_game( game )
            first_story.save()
            return redirect( '/game/' + str( game.id ) )
        else:
            form = game_form
    else:
        form = GameCreationForm( initial={
            'creator': request.user.id
        } )
    return render( request, 'flow/form.html', {
        'form': form,
        'form_name': _( 'Create New Game' ),
        'submit_action_name': _( 'Create Game' ),
        'submit_action_url': '/game/create',
    } )


def game_by_id( request, game_id ):
    try:
        game = Game.objects.get( pk=game_id )
    except Game.DoesNotExist:
        raise Http404( "Game does not exist" )
    return HttpResponse( str( game ) )
