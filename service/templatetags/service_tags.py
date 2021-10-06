from django import template
from django.db.models import Q
from django.utils import timezone
from datetime import datetime as dt
from django.shortcuts import get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError
from service.models import *
from reception.settings import LOCAL_TIMEZONE
from service.models import StateDuty
from user.models import District

register = template.Library()


@register.simple_tag(takes_context=True)
def get_calculated_payments(context, state_duty_id):
    try:
        request = context.get('request')
        startdate = timezone.now().replace(year=2021, month=1, day=1,hour=00,minute=00, second=00)
        stopdate = timezone.now()
        
        if request.GET.get('parent_section', None):
            if request.GET.get('parent_section').isdigit():
                parent_sections = Section.objects.filter(id=request.GET.get('parent_section'), parent__isnull=True, is_active=True)
            else:
                parent_sections = Section.objects.filter(parent__isnull=True, is_active=True)
                

        if request.GET.get('parent_section', None) and request.GET.get('child_section', None):
            if request.GET.get('parent_section').isdigit() and request.GET.get('child_section').isdigit():
                child_sections = Section.objects.filter(id=request.GET.get('child_section'), is_active=True, parent__isnull=False)
            else:
                child_sections = Section.objects.filter(parent__in=parent_sections)
        else:
            child_sections = Section.objects.filter(parent__isnull=False)

        if request.GET.get('startdate', None):
            startdate = dt.strptime(request.GET['startdate'], "%Y-%m-%d").replace(tzinfo=LOCAL_TIMEZONE,hour=00,
                                                                                minute=00, second=00)


        if request.GET.get('stopdate', None):
            stopdate = dt.strptime(request.GET['stopdate'], '%Y-%m-%d').replace(tzinfo=LOCAL_TIMEZONE, hour=23,
                                                                                minute=59, second=59)

        
        total = 0
        paid = 0
        unpaid = 0

        for child_section in child_sections:
            print(child_section)
            print(StateDuty.objects.filter(service__application_service__section=child_section))
            total_qs = StateDuty.objects.filter(
                Q(service__application_service__section=child_section) &
                Q(title=state_duty_id) &
                Q(is_active=True) &
                Q(created_date__range=[startdate, stopdate]) &
                Q(service__application_service__is_active=True) &
                Q(service__application_service__is_block__in=[False] if child_section.pay_for_service else [True, False])
            )

            paid_qs = total_qs.filter(is_paid=True)
            unpaid_qs = total_qs.filter(is_paid=False)

            for item in total_qs:
                total += item.payment
            for item in paid_qs:
                paid += item.payment
            for item in unpaid_qs:
                unpaid += item.payment
        return {
            'total': total,
            'paid': paid,
            'unpaid': unpaid
        }
    except:
        return {
            'total': 0,
            'paid': 0,
            'unpaid': 0
        }


@register.simple_tag
def get_services_list():
    services_list = Service.objects.order_by('sort')
    return services_list