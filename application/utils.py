import itertools
from datetime import datetime as dt
import datetime

from django.db.models import Q
from django.utils import timezone

from application.models import ApplicationDocument
from reception.settings import LOCAL_TIMEZONE
from service.models import (
    FINE,
    TECHNICAL_PASSPORT,
    REGISTRATION,
    RE_REGISTRATION,
    INSPECTION,
    ROAD_FUND,
    ROAD_FUND_HORSE_POWER,
    StateDutyPercent
)


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

        today_min = timezone.now().replace(tzinfo=LOCAL_TIMEZONE, hour=0, minute=0, second=0)
        today_max = timezone.now().replace(tzinfo=LOCAL_TIMEZONE, hour=23, minute=59, second=59)
        some_day_last_week = (timezone.now() - datetime.timedelta(days=7)).replace(tzinfo=LOCAL_TIMEZONE, hour=0,
                                                                                   minute=0, second=0)
        some_day_last_month = timezone.now().replace(day=1, hour=0, minute=0, second=0, tzinfo=LOCAL_TIMEZONE)
        some_day_last_year = timezone.now().replace(day=1, month=1, hour=0, minute=0, second=0, tzinfo=LOCAL_TIMEZONE)

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


def reg_new_car(application, ten_day):
    # Agarda avtomobil davlat raqam belgisi auksionda olingan bo'lsa
    if application.car.is_auction:
        # Agarda 10 kundan oshgan bo'lsa jarima hisob raqamlari va boshqa hisob raqamlar
        if datetime.datetime.now().date() >= ten_day:
            query1 = StateDutyPercent.objects.filter(
                Q(service=application.service, person_type=application.person_type, state_duty=REGISTRATION,
                  is_auction=True) | Q(service=application.service, person_type=application.person_type,
                                       state_duty=TECHNICAL_PASSPORT) | Q(
                    lost_technical_passport=False, state_duty=FINE))
        else:
            query1 = StateDutyPercent.objects.filter(
                Q(service=application.service, person_type=application.person_type, car_is_new=True))
    else:
        # Agarda 10 kundan oshgan bo'lsa jarima hisob raqamlari va boshqa hisob raqamlar
        if datetime.datetime.now().date() >= ten_day:
            query1 = StateDutyPercent.objects.filter(
                Q(service=application.service, person_type=application.person_type, car_is_new=True) | Q(
                    lost_technical_passport=False, state_duty=FINE))
        else:
            query1 = StateDutyPercent.objects.filter(
                Q(service=application.service, person_type=application.person_type, car_is_new=True))
    return query1


def reg_new_car_v2(application):
    car = application.car
    qs = StateDutyPercent.objects.none()

    application_document = ApplicationDocument.objects.filter(application=application,
                                                              example_document__key=application.service.key).last()

    """Jarima"""
    if application_document:
        last_day_without_fine = application_document.contract_date + datetime.timedelta(days=10)
        if datetime.datetime.now().date() > last_day_without_fine if last_day_without_fine.weekday() != 6 else last_day_without_fine + datetime.timedelta(
                days=1):
            """Shartnoma tuzilgan sana 10 kundan kechikganligi uchun jarima"""
            fine1 = StateDutyPercent.objects.filter(service=application.service, state_duty=FINE, lost_technical_passport=False)
            """Qayd etish guvohnomasi yo'qolgan yoki yo'qolmaganligidan kelib chiqib jarima"""
            fine2 = StateDutyPercent.objects.filter(service=application.service, state_duty=FINE,
                                                    lost_technical_passport=car.lost_technical_passport)
            """Ikkala jarimani birlashtirish"""
            qs = (fine1 | fine2).distinct()
        elif car.lost_technical_passport:
            """Qayd etish guvohnomasi yo'qolgan yoki yo'qolmaganligidan kelib chiqib jarima"""
            qs = StateDutyPercent.objects.filter(service=application.service, state_duty=FINE, lost_technical_passport=True)

    """Qayta ro'yhatlash"""
    re_registration = StateDutyPercent.objects.filter(service=application.service, state_duty=RE_REGISTRATION)
    qs = qs.union(re_registration)

    """Ro'yhatlash ya'ni DRB uchun to'lov"""
    if not car.is_auction:
        registration = StateDutyPercent.objects.filter(service=application.service, car_type=car.type,
                                                       lost_number=car.lost_number, is_old_number=car.is_old_number,
                                                       is_auction=car.is_auction,
                                                       car_is_new=car.is_new, state_duty=REGISTRATION)
    else:
        registration = StateDutyPercent.objects.filter(service=application.service, car_type=car.type,
                                                       person_type=application.person_type, lost_number=car.lost_number,
                                                       is_old_number=car.is_old_number,
                                                       car_is_new=car.is_new, is_auction=car.is_auction,
                                                       state_duty=REGISTRATION)
    qs = qs.union(registration)

    """Yangi qayd etish guvohnomasi"""
    technical_passport = StateDutyPercent.objects.filter(state_duty=TECHNICAL_PASSPORT)
    qs = qs.union(technical_passport)

    """Texnik ko'rik"""
    if not car.is_new:
        inspection = StateDutyPercent.objects.filter(service=application.service, person_type=application.person_type,
                                                     car_type=car.type,
                                                     state_duty=INSPECTION)
        qs = qs.union(inspection)

    """Yo'l fondi"""
    some_day_3years_ago = datetime.datetime.now().date().replace(year=datetime.datetime.now().year - 3)
    some_day_7years_ago = datetime.datetime.now().date().replace(year=datetime.datetime.now().year - 7)

    if car.is_new and car.model.is_local:
        """Yangi va mahalliy avtomobil"""
        state_percent = StateDutyPercent.objects.none()
    elif car.is_new and not car.model.is_local:
        """Yangi lekin mahalliy bo'lmagan avtomobil"""
        state_percent = StateDutyPercent.objects.filter(state_duty=ROAD_FUND, service=application.service)
    else:
        # ishlab chiqarilganiga 3 yil to'lmagan
        if some_day_3years_ago <= car.made_year:
            # print('3 yil bo\'lmagan')
            state_percent = StateDutyPercent.objects.filter(service=application.service,
                                                            state_duty=ROAD_FUND_HORSE_POWER, car_type=car.type,
                                                            start=0,
                                                            stop=3)
        # 3 yil to'lgan lekin 7 yil to'lmagan
        elif some_day_3years_ago >= car.made_year and some_day_7years_ago <= car.made_year:
            # print('3 yil bo\'lgan 7 yil bo\'lmagan')
            state_percent = StateDutyPercent.objects.filter(service=application.service,
                                                            state_duty=ROAD_FUND_HORSE_POWER, car_type=car.type,
                                                            start=3,
                                                            stop=7)
        # 7 yildan ortiq
        elif some_day_7years_ago >= car.made_year:
            # print(' 7 yildan o\'tgan')
            state_percent = StateDutyPercent.objects.filter(service=application.service,
                                                            state_duty=ROAD_FUND_HORSE_POWER, car_type=car.type,
                                                            start=7,
                                                            stop=0)
        else:
            state_percent = StateDutyPercent.objects.none()
    qs = qs.union(state_percent)
    return qs
