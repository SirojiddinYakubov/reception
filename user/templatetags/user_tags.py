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
            sections_count = Section.objects.filter(region=region,is_active=True, parent__isnull=False).count()
            print(sections_count)
            return sections_count
        else:
            return 0

    except:
        return 0