from django.contrib.contenttypes.models import ContentType
from .models import Action



def create_action(kind, target=None):

    action = Action(kind=kind, target=target)
    action.save()
    return action