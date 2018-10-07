from django.contrib.auth import login
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.utils.translation import gettext as _

from flow.access_helper import is_editor
from .models import Game, Editors, Story, User
from .forms import SignupForm, GameCreationForm, StoryForm
from .default_models import first_story_on_new_game, new_story_on_game


def index( request ):
    return render( request, 'flow/index.html', {
        'user_name': 'carl'
    } )


def signup( request ):
    if request.method == 'POST':
        form = SignupForm( request.POST )
        if form.is_valid():
            user = User.objects.create_user(
                username=form[ 'username' ].value(),
                email=form[ 'email' ].value(),
                password=form[ 'password' ].value()
            )
            user.first_name = form[ 'first_name' ].value()
            user.last_name = form[ 'last_name' ].value()
            user.profile_picture = form[ 'profile_picture' ].value()
            user.save()
            login( request, user )
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
            game.first_story = first_story
            game.save()
            Editors.objects.create( user=request.user, game=game )
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
    return render( request, 'flow/game.html', {
        'game': game,
        'is_editor': is_editor( game_id, request.user )
    } )


def edit_game( request, game_id ):
    try:
        game = Game.objects.get( pk=game_id )
    except Game.DoesNotExist:
        raise Http404( _( "Game does not exist" ) )
    if not is_editor( game_id, request.user ):
        raise PermissionDenied( _( 'You are not an editor of this game' ) )

    return render( request, 'flow/edit_game.html', {
        'game': game,
        'stories': Story.objects.filter( game_id=game_id ),
    } )


def edit_story( request, game_id, story_id ):
    try:
        game = Game.objects.get( pk=game_id )
        story = Story.objects.get( pk=story_id )
    except Game.DoesNotExist:
        raise Http404( _( "Game or story does not exist" ) )

    if request.method == 'POST':
        story_form = StoryForm( request.POST, instance=story )
        if story_form.is_valid():
            story_form.save()
            redirect( 'index' )
    if not is_editor( game_id, request.user ):
        raise PermissionDenied( _( 'You are not an editor of this game' ) )

    story_form = StoryForm( instance=story )

    return render( request, 'flow/edit_story.html', {
        'game': game,
        'story_form': story_form,
        'form_submit_action': request.get_full_path()
    } )


def add_story( request, game_id ):
    try:
        game = Game.objects.get( pk=game_id )
    except Game.DoesNotExist:
        raise Http404( _( "Game or story does not exist" ) )
    story = new_story_on_game( game )
    story.save()
    return redirect( 'edit_story', game_id=game_id, story_id=story.id )
