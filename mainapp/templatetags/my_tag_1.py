from django import template
from django.conf import settings

register = template.Library()


# @register.filter(name='media_def_good')
def media_default_good(string):
    if not string:
        string = 'product_images/good_default.png'
    return f'{settings.MEDIA_URL}{string}'


@register.filter(name='media_def_usr')
def media_default_users(string):
    if not string:
        string = 'avatars/user_default.png'
    return f'{settings.MEDIA_URL}{string}'


register.filter('media_def_good', media_default_good)
