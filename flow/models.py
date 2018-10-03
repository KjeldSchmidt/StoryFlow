from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User( AbstractUser ):
    profile_picture = models.ImageField( blank=True, null=True )


class Game( models.Model ):
    creator = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
    name = models.CharField( max_length=50 )
    description = models.CharField( max_length=1000 )
    first_story = models.ForeignKey( 'Story', on_delete=models.CASCADE, related_name='+', blank=True, null=True )


class Story( models.Model ):
    text = models.CharField( max_length=10000 )
    game = models.ForeignKey( Game, on_delete=models.CASCADE )
    comment = models.CharField( max_length=10000 )
    name = models.CharField( max_length=100 )
    background = models.FilePathField( default=None, null=True )


class Playthrough( models.Model ):
    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
    game = models.ForeignKey( Game, on_delete=models.CASCADE )
    story_position = models.ForeignKey( Story, on_delete=models.CASCADE )
    last_save = models.DateTimeField( auto_now=True )


class Condition( models.Model ):
    condition = models.CharField( max_length=1000 )


class Choice( models.Model ):
    condition_to_show = models.ForeignKey( Condition, on_delete=models.CASCADE )
    text = models.CharField( max_length=500 )
    actions = models.CharField( max_length=200 )
    comment = models.CharField( max_length=10000 )
    name = models.CharField( max_length=100 )


class StoryChoiceMap( models.Model ):
    story = models.ForeignKey( Story, on_delete=models.CASCADE )
    choice = models.ForeignKey( Choice, on_delete=models.CASCADE )


class FollowCondition( models.Model ):
    order = models.PositiveSmallIntegerField()
    choice = models.ForeignKey( Choice, on_delete=models.CASCADE )
    condition = models.ForeignKey( Condition, on_delete=models.CASCADE )
    follow_story = models.ForeignKey( Story, on_delete=models.CASCADE )


class Stat( models.Model ):
    game = models.ForeignKey( Game, on_delete=models.CASCADE )
    name = models.CharField( max_length=20 )
    max = models.IntegerField()
    min = models.IntegerField()
    is_secret = models.BooleanField()


class TextVariable( models.Model ):
    game = models.ForeignKey( Game, on_delete=models.CASCADE )
    name = models.CharField( max_length=20 )
    is_secret = models.BooleanField()


class State( models.Model ):
    playtrough = models.ForeignKey( Playthrough, on_delete=models.CASCADE )
    stat = models.ForeignKey( Stat, on_delete=models.CASCADE )
    value = models.IntegerField()


class Textvars( models.Model ):
    playtrough = models.ForeignKey( Playthrough, on_delete=models.CASCADE )
    stat = models.ForeignKey( TextVariable, on_delete=models.CASCADE )
    value = models.CharField( max_length=20 )


class StoryPositionVar( models.Model ):
    playtrough_id = models.ForeignKey( Playthrough, on_delete=models.CASCADE )
    story_id = models.ForeignKey( Story, on_delete=models.CASCADE )
    name = models.CharField( max_length=30 )


class Editors( models.Model ):
    game = models.ForeignKey( Game, on_delete=models.CASCADE )
    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE )


class EditorChangeMessage( models.Model ):
    creator = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
    game = models.ForeignKey( Game, on_delete=models.CASCADE )
    message = models.CharField( max_length=1000 )
    timestamp = models.DateTimeField( auto_now_add=True )


class StoryTag( models.Model ):
    story = models.ForeignKey( Story, on_delete=models.CASCADE )
    tag = models.CharField( max_length=20 )
