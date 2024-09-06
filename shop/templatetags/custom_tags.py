from django import template
from django.contrib.sessions.models import Session
# from django.http import request



register = template.Library()

@register.filter(name="sessioncheck")
def sessioncheck(l,k):
             return l.get(str(k))
           