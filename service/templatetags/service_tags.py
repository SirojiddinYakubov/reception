from django import template
from django.db.models import Q
from django.utils import timezone
from datetime import datetime as dt

from django.utils.datastructures import MultiValueDictKeyError

from reception.settings import LOCAL_TIMEZONE
from service.models import StateDuty
from user.models import District

register = template.Library()


@register.simple_tag(takes_context=True)
def get_calculated_payments(context, state_duty_id):
    try:
        request = context.get('request')
        startdate = timezone.now().replace(year=2021, month=1, day=1)
        stopdate = timezone.now()
        region = request.user.section.region
        districts = request.user.section.district.all()

        try:
            if request.GET['startdate', None] and request.GET['startdate'] != 'None' and request.GET['startdate'] != '':
                startdate = dt.strptime(request.GET['startdate'], "%Y-%m-%d").replace(tzinfo=LOCAL_TIMEZONE)
        except MultiValueDictKeyError:
            pass

        try:
            if request.GET['stopdate'] and request.GET['stopdate'] != 'None' and request.GET['stopdate'] != '':
                stopdate = dt.strptime(request.GET['stopdate'], '%Y-%m-%d').replace(tzinfo=LOCAL_TIMEZONE, hour=23,
                                                                                    minute=59, second=59)
        except MultiValueDictKeyError:
            pass

        try:
            if request.GET['district'] and request.GET['district'] != 'all':
                region = request.user.section.region
                districts = District.objects.filter(id=request.GET['district'])
        except MultiValueDictKeyError:
            pass

        payments = StateDuty.objects.filter(Q(Q(service__application_service__created_user__region=region) & Q(
            service__application_service__created_user__district__in=districts) & Q(
            service__organization__isnull=True)) | Q(
            Q(service__organization__legal_address_region=region) & Q(
                service__organization__legal_address_district__in=districts) & Q(
                service__organization__isnull=False))).filter(
            Q(title=state_duty_id) & Q(is_active=True) & Q(created_date__range=[startdate, stopdate]) & Q(
                service__application_service__is_active=True) & Q(service__application_service__is_block=False))

        total = 0
        for payment in payments:
            total += payment.payment
        return total
    except:
        return 0


@register.simple_tag(takes_context=True)
def get_paid_payments(context, state_duty_id):
    try:
        request = context.get('request')
        startdate = timezone.now().replace(year=2021, month=1, day=1)
        stopdate = timezone.now()
        region = request.user.section.region
        districts = request.user.section.district.all()

        try:
            if request.GET['startdate', None] and request.GET['startdate'] != 'None' and request.GET['startdate'] != '':
                startdate = dt.strptime(request.GET['startdate'], "%Y-%m-%d").replace(tzinfo=LOCAL_TIMEZONE)
        except MultiValueDictKeyError:
            pass

        try:
            if request.GET['stopdate'] and request.GET['stopdate'] != 'None' and request.GET['stopdate'] != '':
                stopdate = dt.strptime(request.GET['stopdate'], '%Y-%m-%d').replace(tzinfo=LOCAL_TIMEZONE, hour=23,
                                                                                    minute=59, second=59)
        except MultiValueDictKeyError:
            pass

        try:
            if request.GET['district'] and request.GET['district'] != 'all':
                region = request.user.section.region
                districts = District.objects.filter(id=request.GET['district'])
        except MultiValueDictKeyError:
            pass

        payments = StateDuty.objects.filter(Q(Q(service__application_service__created_user__region=region) & Q(
            service__application_service__created_user__district__in=districts) & Q(
            service__organization__isnull=True)) | Q(
            Q(service__organization__legal_address_region=region) & Q(
                service__organization__legal_address_district__in=districts) & Q(
                service__organization__isnull=False))).filter(
            Q(title=state_duty_id) & Q(is_active=True) & Q(created_date__range=[startdate, stopdate]) & Q(
                is_paid=True) & Q(service__application_service__is_active=True) & Q(
                service__application_service__is_block=False))

        total = 0
        for payment in payments:
            total += payment.payment
        return total
    except:
        return 0


@register.simple_tag(takes_context=True)
def get_unpaid_payments(context, state_duty_id):
    try:
        request = context.get('request')
        startdate = timezone.now().replace(year=2021, month=1, day=1)
        stopdate = timezone.now()
        region = request.user.section.region
        districts = request.user.section.district.all()

        try:
            if request.GET['startdate', None] and request.GET['startdate'] != 'None' and request.GET['startdate'] != '':
                startdate = dt.strptime(request.GET['startdate'], "%Y-%m-%d").replace(tzinfo=LOCAL_TIMEZONE)
        except MultiValueDictKeyError:
            pass

        try:
            if request.GET['stopdate'] and request.GET['stopdate'] != 'None' and request.GET['stopdate'] != '':
                stopdate = dt.strptime(request.GET['stopdate'], '%Y-%m-%d').replace(tzinfo=LOCAL_TIMEZONE, hour=23,
                                                                                    minute=59, second=59)
        except MultiValueDictKeyError:
            pass

        try:
            if request.GET['district'] and request.GET['district'] != 'all':
                region = request.user.section.region
                districts = District.objects.filter(id=request.GET['district'])
        except MultiValueDictKeyError:
            pass

        payments = StateDuty.objects.filter(Q(Q(service__application_service__created_user__region=region) & Q(
            service__application_service__created_user__district__in=districts) & Q(
            service__organization__isnull=True)) | Q(
            Q(service__organization__legal_address_region=region) & Q(
                service__organization__legal_address_district__in=districts) & Q(
                service__organization__isnull=False))).filter(
            Q(title=state_duty_id) & Q(is_active=True) & Q(created_date__range=[startdate, stopdate]) & Q(
                is_paid=False) & Q(service__application_service__is_active=True) & Q(
                service__application_service__is_block=False))

        total = 0
        for payment in payments:
            total += payment.payment
        return total
    except:
        return 0
