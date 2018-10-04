from flow.models import Editors


def is_editor( game_id, user ) -> bool:
    """
    Validates that the user currently logged in is an editor of the game to be accessed.

    :param game_id: ID of the game to access
    :param user: a user, probably the one currently logged in
    :return: Boolean
    """
    return Editors.objects.filter( game_id=game_id, user_id=user.id ).exists()
