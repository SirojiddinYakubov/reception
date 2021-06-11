from datetime import datetime as dt
import datetime
from django.utils import timezone

from reception.settings import LOCAL_TIMEZONE


def application_right_filters(qs, request_get):

    if request_get.get('service'):
        key = request_get.get('service')
        if key == 'account_statement':
            qs = qs.filter(service__title='account_statement')
        if key == 'gift_agreement':
            qs = qs.filter(service__title='gift_agreement')
        if key == 'contract_of_sale':
            qs = qs.filter(service__title='contract_of_sale')
        if key == 'replace_tp':
            qs = qs.filter(service__title='replace_tp')
        if key == 'replace_number_and_tp':
            qs = qs.filter(service__title='replace_number_and_tp')

    if request_get.get('person_type'):
        qs = qs.filter(person_type=request_get.get('person_type'))

    if request_get.get('process'):
        qs = qs.filter(process=request_get.get('process'))

    if request_get.get('payment'):
        qs = qs.filter(is_payment=request_get.get('payment'))

    if request_get.get('confirm'):
        qs = qs.filter(service__car__is_confirm=request_get.get('confirm'))

    if request_get.get('technical_confirm'):
        qs = qs.filter(service__car__is_technical_confirm=request_get.get('technical_confirm'))


    if request_get.get('date'):

        today_min = timezone.now().replace(tzinfo=LOCAL_TIMEZONE, hour=0,minute=0,second=0)
        today_max = timezone.now().replace(tzinfo=LOCAL_TIMEZONE, hour=23,minute=59,second=59)
        some_day_last_week = (timezone.now() - datetime.timedelta(days=7)).replace(tzinfo=LOCAL_TIMEZONE, hour=0,minute=0, second=0)
        some_day_last_month = timezone.now().replace(day=1,hour=0,minute=0,second=0,tzinfo=LOCAL_TIMEZONE)
        some_day_last_year = timezone.now().replace(day=1,month=1,hour=0,minute=0,second=0,tzinfo=LOCAL_TIMEZONE)

        print(qs.first().created_date)
        print(today_min)
        print(today_max)
        print(some_day_last_week)
        print(some_day_last_month)
        print(some_day_last_year)
        if request_get.get('date') == 'today':
            qs = qs.filter(created_date__range=(today_min, today_max))

        if request_get.get('date') == 'last-7-days':
            qs = qs.filter(created_date__range=(some_day_last_week, today_max))

        if request_get.get('date') == 'month':
            qs = qs.filter(created_date__range=(some_day_last_month, today_max))

        if request_get.get('date') == 'year':
            qs = qs.filter(created_date__range=(some_day_last_year, today_max))


    return qs