from django import template
from django.conf import settings

from snippets.models import Snippet

register = template.Library()


@register.simple_tag
def snippet(title):
    try:
        return Snippet.objects.get(title=title).body
    except Snippet.DoesNotExist:
        if settings.DEBUG:
            return "<span>Can't find Snippet %s</span>" % (title,)
        else:
            return '' 
