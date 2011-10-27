import re

from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter
@stringfilter
def seo_friendlify(value):
    """
    Return an SEO-friendly string to be used in a URL.

    Lower all letters, replace all spaces with dashes, and strip anything
    that isn't a letter, number, underscore or dash.
    
    Arguments:
    - `value`: The input string to be url-friendlified.

    Example:
    - "My friendly string" --> "my-friendly-string"
    """
    return re.sub('[^-a-z0-9_]', '', value.lower().replace(' ', '-'))

seo_friendlify.is_safe = True
