'''
Created on Aug 20, 2018

@author: Satavan
'''
import hashlib
from urllib.parse import urlencode

from django import template
from django.conf import settings

register = template.Library()


@register.filter
def gravatar(user):
#     email = user.email.lower().encode('utf-8')
    email = "prsh.jkd123@gmail.com".lower().encode('utf-8') ## hard coded
    default = 'mm'
    size = 256
    url = 'https://www.gravatar.com/avatar/{md5}?{params}'.format(
        md5=hashlib.md5(email).hexdigest(),
        params=urlencode({'d': default, 's': str(size)})
    )
    return url