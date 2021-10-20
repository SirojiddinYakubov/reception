import datetime
from urllib.parse import urlencode

from django import template
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils import timezone

from application.models import Application
from user.models import *

register = template.Library()


@register.simple_tag
def get_parent_null_sections_count(section_id):
    try:
        section = get_object_or_404(Section, id=section_id)
        if section.parent == None:
            region = get_object_or_404(Region, id=section.region.id)
            sections_count = Section.objects.filter(region=region, is_active=True, parent__isnull=False).count()
            return sections_count
        else:
            return 0

    except:
        return 0


@register.simple_tag(name='get_user_notifications', takes_context=True)
def get_user_notifications(context):
    request = context['request']
    notifications = Notification.objects.filter(is_active=True, receiver=request.user)
    not_read_count = Notification.objects.filter(is_active=True, is_read=False, receiver=request.user).count()
    context = {
        'notifications': notifications,
        "not_read_count": not_read_count
    }
    return context
