from datetime import datetime, timezone

from reception.settings import LOCAL_TIMEZONE


def application_right_filters(qs, request_get):
    print(request_get)
    if request_get.get('service'):
        key = request_get.get('service')
        if key == 'account_statement':
            qs = qs.filter(service__title='account_statement')
            return qs
        if key == 'gift_agreement':
            qs = qs.filter(service__title='gift_agreement')
            return qs
        if key == 'contract_of_sale':
            qs = qs.filter(service__title='contract_of_sale')
            print(qs)
            return qs
        print(20)
        if key == 'replace_tp':
            qs = qs.filter(service__title='replace_tp')
            return qs
        if key == 'replace_number_and_tp':
            qs = qs.filter(service__title='replace_number_and_tp')
            return qs
    if request_get.get('person_type'):
        qs = qs.filter(person_type=request_get.get('person_type'))
        return qs
    if request_get.get('process'):
        qs = qs.filter(process=request_get.get('process'))
        return qs
    if request_get.get('payment'):
        qs = qs.filter(is_payment=request_get.get('payment'))
        return qs
    if request_get.get('confirm'):
        qs = qs.filter(service__car__is_confirm=request_get.get('confirm'))
        return qs
    if request_get.get('technical_confirm'):
        qs = qs.filter(service__car__is_technical_confirm=request_get.get('technical_confirm'))
        return qs
    print('good')
    if request_get.get('date'):
        print('ok')
        today_min = timezone.now().replace(tzinfo=LOCAL_TIMEZONE, hour=0,minute=0,second=0)
        today_max = timezone.now().replace(tzinfo=LOCAL_TIMEZONE, hour=23,minute=59,second=59)
        some_day_last_week = (timezone.now() - datetime.timedelta(days=7)).replace(tzinfo=LOCAL_TIMEZONE, hour=0,minute=0, second=0)

        some_day_last_month = datetime.datetime.combine(today_min.replace(day=1), datetime.time.min)
        some_day_last_year = datetime.datetime.combine(today_min.replace(month=1, day=1), datetime.time.min)

        print(today_min)
        print(today_max)
        print(some_day_last_week)
        print(some_day_last_month)
        print(some_day_last_year)
        if request_get.get('date') == 'today':
            qs = qs.filter(created_date__range=(today_min, today_max))
            return qs
        if request_get.get('date') == 'last-7-days':
            qs = qs.filter(created_date__range=(some_day_last_week, today_max))
            return qs
        if request_get.get('date') == 'month':
            qs = qs.filter(created_date__range=(some_day_last_month, today_max))
            return qs
        if request_get.get('date') == 'year':
            qs = qs.filter(created_date__range=(some_day_last_year, today_max))
            return qs

    return qs