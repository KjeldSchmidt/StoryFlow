from django.utils.translation import gettext as _

from .models import Story, Game


def first_story_on_new_game( game: Game ) -> Story:
    story = Story()
    story.game = game
    story.name = _( 'It all begins here' )
    story.text = _( 'Once upon a time... \n\n This is where your story starts - the very first text your players see' )
    story.comment = _( 'This is a comment. It is only visible to you and other editors of the game, never to players. Use it to communicate with yourself over time or with your teammates.' )
    story.background = None
    return story
