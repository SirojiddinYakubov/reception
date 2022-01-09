import itertools
from datetime import datetime as dt
import datetime
from typing import Dict

from django.db.models import Q, QuerySet
from django.utils import timezone

from api.v1.landing.serializers import CalculateSerializer
from application.models import ApplicationDocument, Application
from reception.settings import LOCAL_TIMEZONE
from service.models import (
    FINE,
    TECHNICAL_PASSPORT,
    REGISTRATION,
    RE_REGISTRATION,
    INSPECTION,
    ROAD_FUND,
    ROAD_FUND_HORSE_POWER,
    StateDutyPercent, Service, AmountBaseCalculation
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

        if request_get.get('date') == 'today':
            qs = qs.filter(created_date__range=(today_min, today_max))

        if request_get.get('date') == 'last-7-days':
            qs = qs.filter(created_date__range=(some_day_last_week, today_max))

        if request_get.get('date') == 'month':
            qs = qs.filter(created_date__range=(some_day_last_month, today_max))

        if request_get.get('date') == 'year':
            qs = qs.filter(created_date__range=(some_day_last_year, today_max))

    return qs


# def reg_new_car(application, ten_day):
#     # Agarda avtomobil davlat raqam belgisi auksionda olingan bo'lsa
#     if application.car.is_auction:
#         # Agarda 10 kundan oshgan bo'lsa jarima hisob raqamlari va boshqa hisob raqamlar
#         if datetime.datetime.now().date() >= ten_day:
#             query1 = StateDutyPercent.objects.filter(
#                 Q(service=application.service, person_type=application.person_type, state_duty=REGISTRATION,
#                   is_auction=True) | Q(service=application.service, person_type=application.person_type,
#                                        state_duty=TECHNICAL_PASSPORT) | Q(
#                     lost_technical_passport=False, state_duty=FINE))
#         else:
#             query1 = StateDutyPercent.objects.filter(
#                 Q(service=application.service, person_type=application.person_type, car_is_new=True))
#     else:
#         # Agarda 10 kundan oshgan bo'lsa jarima hisob raqamlari va boshqa hisob raqamlar
#         if datetime.datetime.now().date() >= ten_day:
#             query1 = StateDutyPercent.objects.filter(
#                 Q(service=application.service, person_type=application.person_type, car_is_new=True) | Q(
#                     lost_technical_passport=False, state_duty=FINE))
#         else:
#             query1 = StateDutyPercent.objects.filter(
#                 Q(service=application.service, person_type=application.person_type, car_is_new=True))
#     return query1


# def reg_new_car_v2(application):
#     car = application.car
#     qs = StateDutyPercent.objects.none()
#
#     application_document = ApplicationDocument.objects.filter(application=application,
#                                                               example_document__key=application.service.key).last()
#
#     """Jarima"""
#     if application_document:
#         last_day_without_fine = application_document.contract_date + datetime.timedelta(days=10)
#
#         if last_day_without_fine.weekday() == 6:
#             last_day_without_fine = last_day_without_fine + datetime.timedelta(days=1)
#
#         if datetime.datetime.now().date() > last_day_without_fine:
#             """Shartnoma tuzilgan sana 10 kundan kechikganligi uchun jarima"""
#             fine1 = StateDutyPercent.objects.filter(service=application.service, state_duty=FINE,
#                                                     lost_technical_passport=False, )
#             """Qayd etish guvohnomasi yo'qolgan yoki yo'qolmaganligidan kelib chiqib jarima"""
#             fine2 = StateDutyPercent.objects.filter(service=application.service, state_duty=FINE,
#                                                     lost_technical_passport=car.lost_technical_passport)
#             """Ikkala jarimani birlashtirish"""
#             qs = (fine1 | fine2).distinct()
#         elif car.lost_technical_passport:
#             """Qayd etish guvohnomasi yo'qolgan yoki yo'qolmaganligidan kelib chiqib jarima"""
#             qs = StateDutyPercent.objects.filter(service=application.service, state_duty=FINE,
#                                                  lost_technical_passport=True)
#     else:
#         if car.lost_technical_passport:
#             qs = StateDutyPercent.objects.filter(service=application.service, state_duty=FINE,
#                                                  lost_technical_passport=True)
#     """Qayta ro'yhatlash"""
#     re_registration = StateDutyPercent.objects.filter(service=application.service, state_duty=RE_REGISTRATION)
#     qs = qs.union(re_registration)
#
#     """Ro'yhatlash ya'ni DRB uchun to'lov"""
#     if not car.is_auction:
#         if car.save_old_number:
#             registration = StateDutyPercent.objects.filter(service=application.service, car_type=car.type,
#                                                            lost_number=False, is_old_number=car.is_old_number,
#                                                            is_auction=False,
#                                                            car_is_new=False, is_save_old_number=car.save_old_number,
#                                                            state_duty=REGISTRATION, )
#
#         else:
#             registration = StateDutyPercent.objects.filter(service=application.service, car_type=car.type,
#                                                            lost_number=car.lost_number, is_old_number=car.is_old_number,
#                                                            is_auction=False,
#                                                            car_is_new=car.is_new,
#                                                            is_save_old_number=car.save_old_number,
#                                                            state_duty=REGISTRATION)
#     else:
#         registration = StateDutyPercent.objects.filter(service=application.service, car_type=car.type,
#                                                        person_type=application.person_type, lost_number=car.lost_number,
#                                                        is_old_number=car.is_old_number,
#                                                        car_is_new=car.is_new, is_auction=car.is_auction,
#                                                        is_save_old_number=car.save_old_number,
#                                                        state_duty=REGISTRATION)
#     qs = qs.union(registration)
#
#     """Yangi qayd etish guvohnomasi"""
#     technical_passport = StateDutyPercent.objects.filter(state_duty=TECHNICAL_PASSPORT)
#     qs = qs.union(technical_passport)
#
#     """Texnik ko'rik"""
#     if not car.is_new:
#         inspection = StateDutyPercent.objects.filter(service=application.service, person_type=application.person_type,
#                                                      car_type=car.type,
#                                                      state_duty=INSPECTION)
#         qs = qs.union(inspection)
#
#     """Yo'l fondi"""
#     some_day_3years_ago = datetime.datetime.now().date().replace(year=datetime.datetime.now().year - 3)
#     some_day_7years_ago = datetime.datetime.now().date().replace(year=datetime.datetime.now().year - 7)
#
#     if car.is_new and car.model.is_local:
#         """Yangi va mahalliy avtomobil"""
#         if car.made_year < datetime.datetime.strptime('25.12.2020', '%d.%m.%Y').date():
#             state_percent = StateDutyPercent.objects.filter(service=application.service, state_duty=ROAD_FUND)
#         else:
#             state_percent = StateDutyPercent.objects.none()
#     elif car.is_new and not car.model.is_local:
#         """Yangi lekin mahalliy bo'lmagan avtomobil"""
#         state_percent = StateDutyPercent.objects.filter(state_duty=ROAD_FUND, service=application.service)
#     else:
#         # ishlab chiqarilganiga 3 yil to'lmagan
#         if some_day_3years_ago <= car.made_year:
#             # print('3 yil bo\'lmagan')
#             state_percent = StateDutyPercent.objects.filter(service=application.service,
#                                                             state_duty=ROAD_FUND_HORSE_POWER, car_type=car.type,
#                                                             start=0,
#                                                             stop=3)
#         # 3 yil to'lgan lekin 7 yil to'lmagan
#         elif some_day_3years_ago >= car.made_year and some_day_7years_ago <= car.made_year:
#             # print('3 yil bo\'lgan 7 yil bo\'lmagan')
#             state_percent = StateDutyPercent.objects.filter(service=application.service,
#                                                             state_duty=ROAD_FUND_HORSE_POWER, car_type=car.type,
#                                                             start=3,
#                                                             stop=7)
#         # 7 yildan ortiq
#         elif some_day_7years_ago >= car.made_year:
#             # print(' 7 yildan o\'tgan')
#             state_percent = StateDutyPercent.objects.filter(service=application.service,
#                                                             state_duty=ROAD_FUND_HORSE_POWER, car_type=car.type,
#                                                             start=7,
#                                                             stop=0)
#         else:
#             state_percent = StateDutyPercent.objects.none()
#     qs = qs.union(state_percent)
#     return qs


def filter_state_duty_percents(data) -> QuerySet[StateDutyPercent]:
    if isinstance(data, dict):
        """Get variables from dict"""
        service_id = data.get('service')
        service = Service.objects.get(id=service_id)
        if service.key == 'account_statement':
            is_new = True
        else:
            is_new = False

        car_type = data.get('type')
        is_local = data.get('is_local')
        person_type = data.get('person_type')
        engine_power = data.get('engine_power')
        price = data.get('price')
        made_year = data.get('made_year')
        if made_year:
            made_year = datetime.datetime.strptime(made_year, '%Y-%m-%d').date()
        contract_date = data.get('contract_date')
        if contract_date:
            contract_date = datetime.datetime.strptime(contract_date, '%Y-%m-%d').date()

        is_auction = data.get('is_auction')
        save_old_number = data.get('save_old_number')
        is_saved_number = data.get('is_saved_number')
        lost_number = data.get('lost_number')
        is_old_number = data.get('is_old_number')
        is_relative = data.get('is_relative')
        lost_technical_passport = data.get('lost_technical_passport')
    else:
        """Get variables from application"""
        service = data.service
        is_new = data.car.is_new
        car_type = data.car.type
        is_local = data.car.model.is_local
        person_type = data.person_type
        engine_power = data.car.engine_power
        price = data.car.price
        made_year = data.car.made_year
        application_document = ApplicationDocument.objects.filter(application=data,
                                                                  example_document__key=data.service.key).last()
        if application_document:
            contract_date = application_document.contract_date
        else:
            contract_date = None
        is_auction = data.car.is_auction
        save_old_number = data.car.save_old_number
        is_saved_number = data.car.is_saved_number
        lost_number = data.car.lost_number
        is_old_number = data.car.is_old_number
        is_relative = data.car.is_relative
        lost_technical_passport = data.car.lost_technical_passport

    """Start filter state duty percents"""
    """Jarima"""
    if contract_date:
        last_day_without_fine = contract_date + datetime.timedelta(days=10)

        if last_day_without_fine.weekday() == 6:
            last_day_without_fine = last_day_without_fine + datetime.timedelta(days=1)

        if datetime.datetime.now().date() > last_day_without_fine:
            """Shartnoma tuzilgan sana 10 kundan kechikganligi uchun jarima"""
            fine1 = StateDutyPercent.objects.filter(service=service, state_duty=FINE,
                                                    contract_fine=True, percent__gt=0)
        else:
            fine1 = StateDutyPercent.objects.none()
    else:
        fine1 = StateDutyPercent.objects.none()

    # """Qayd etish guvohnomasi yo'qolgan yoki yo'qolmaganligidan kelib chiqib jarima"""
    # fine2 = StateDutyPercent.objects.filter(service=service, state_duty=FINE,
    #                                         lost_technical_passport=lost_technical_passport,
    #                                         lost_number=False, contract_fine=False)
    # """Raqam yo'qolganligi uchun jarima"""
    # fine3 = StateDutyPercent.objects.filter(service=service, state_duty=FINE,
    #                                         lost_number=lost_number, lost_technical_passport=False,
    #                                         contract_fine=False)

    """Uchala jarimani birlashtirish"""
    # qs = (fine1 | fine2 | fine3).distinct()
    qs = fine1

    """Qayta ro'yhatlash"""
    re_registration = StateDutyPercent.objects.filter(service=service, state_duty=RE_REGISTRATION, percent__gt=0)
    qs = qs.union(re_registration)

    """Ro'yhatlash ya'ni DRB uchun to'lov"""
    if not is_auction:
        if save_old_number:
            registration1 = StateDutyPercent.objects.filter(service=service, car_type=car_type,
                                                            lost_number=False, is_old_number=is_old_number,
                                                            is_auction=False,
                                                            car_is_new=False,
                                                            is_save_old_number=save_old_number,
                                                            is_saved_number=is_saved_number,
                                                            state_duty=REGISTRATION,
                                                            lost_technical_passport=False,
                                                            percent__gt=0)

        else:
            registration1 = StateDutyPercent.objects.filter(service=service, car_type=car_type,
                                                            lost_number=lost_number,
                                                            is_old_number=is_old_number,
                                                            is_auction=False,
                                                            car_is_new=is_new,
                                                            is_save_old_number=save_old_number,
                                                            is_saved_number=is_saved_number,
                                                            state_duty=REGISTRATION,
                                                            lost_technical_passport=False,
                                                            percent__gt=0)
    else:
        registration1 = StateDutyPercent.objects.filter(service=service, car_type=car_type,
                                                        lost_number=lost_number,
                                                        is_old_number=is_old_number,
                                                        car_is_new=is_new, is_auction=is_auction,
                                                        is_save_old_number=save_old_number,
                                                        is_saved_number=is_saved_number,
                                                        state_duty=REGISTRATION,
                                                        lost_technical_passport=False, percent__gt=0)
    if lost_number:
        """Qayd etish guvohnomasi yo'qolgan yoki yo'qolmaganligidan kelib chiqib jarima"""
        registration2 = StateDutyPercent.objects.filter(service=service, car_type=car_type,
                                                        lost_number=True,
                                                        is_old_number=is_old_number,
                                                        car_is_new=is_new, is_auction=is_auction,
                                                        is_save_old_number=save_old_number,
                                                        is_saved_number=is_saved_number,
                                                        is_relative=is_relative,
                                                        state_duty=REGISTRATION,
                                                        lost_technical_passport=False, percent__gt=0)
    else:
        registration2 = StateDutyPercent.objects.none()

    if lost_technical_passport:
        """Raqam yo'qolganligi uchun jarima"""
        registration3 = StateDutyPercent.objects.filter(service=service, car_type=car_type,
                                                        lost_number=False,
                                                        is_old_number=is_old_number,
                                                        car_is_new=is_new, is_auction=is_auction,
                                                        is_save_old_number=save_old_number,
                                                        is_saved_number=is_saved_number,
                                                        is_relative=is_relative,
                                                        state_duty=REGISTRATION,
                                                        lost_technical_passport=True, percent__gt=0)
    else:
        registration3 = StateDutyPercent.objects.none()
    if lost_technical_passport and lost_number:
        registration4 = (registration2 | registration3)
    else:
        registration4 = StateDutyPercent.objects.none()

    registration = (registration1 | registration2 | registration3 | registration4).distinct()
    qs = qs.union(registration)

    """Yangi qayd etish guvohnomasi"""
    technical_passport = StateDutyPercent.objects.filter(state_duty=TECHNICAL_PASSPORT, percent__gt=0)
    qs = qs.union(technical_passport)

    # """Texnik ko'rik"""
    # if not is_new:
    #     inspection = StateDutyPercent.objects.filter(service=service,
    #                                                  person_type=person_type,
    #                                                  car_type=car_type,
    #                                                  state_duty=INSPECTION)
    #     qs = qs.union(inspection)

    """Yo'l fondi"""
    if contract_date:
        if datetime.datetime.strptime('01.01.2022', '%d.%m.%Y').date() > contract_date:
            some_day_3years_ago = datetime.datetime.now().date().replace(year=datetime.datetime.now().year - 3)
            some_day_7years_ago = datetime.datetime.now().date().replace(year=datetime.datetime.now().year - 7)

            if is_new and is_local:
                """Yangi va mahalliy avtomobil"""
                if made_year < datetime.datetime.strptime('09.10.2019', '%d.%m.%Y').date():
                    state_percent = StateDutyPercent.objects.filter(service=service, state_duty=ROAD_FUND, percent__gt=0)
                else:
                    state_percent = StateDutyPercent.objects.none()
            elif is_new and not is_local:
                """Yangi lekin mahalliy bo'lmagan avtomobil"""
                state_percent = StateDutyPercent.objects.filter(state_duty=ROAD_FUND, service=service, percent__gt=0)
            else:
                # ishlab chiqarilganiga 3 yil to'lmagan
                if some_day_3years_ago <= made_year:
                    # print('3 yil bo\'lmagan')
                    state_percent = StateDutyPercent.objects.filter(service=service,
                                                                    state_duty=ROAD_FUND_HORSE_POWER, car_type=car_type,
                                                                    start=0,
                                                                    stop=3, percent__gt=0)
                # 3 yil to'lgan lekin 7 yil to'lmagan
                elif some_day_3years_ago >= made_year and some_day_7years_ago <= made_year:
                    # print('3 yil bo\'lgan 7 yil bo\'lmagan')
                    state_percent = StateDutyPercent.objects.filter(service=service,
                                                                    state_duty=ROAD_FUND_HORSE_POWER, car_type=car_type,
                                                                    start=3,
                                                                    stop=7, percent__gt=0)
                # 7 yildan ortiq
                elif some_day_7years_ago >= made_year:
                    # print(' 7 yildan o\'tgan')
                    state_percent = StateDutyPercent.objects.filter(service=service,
                                                                    state_duty=ROAD_FUND_HORSE_POWER, car_type=car_type,
                                                                    start=7,
                                                                    stop=0, percent__gt=0)
                else:
                    state_percent = StateDutyPercent.objects.none()

                if is_relative:
                    state_percent = StateDutyPercent.objects.none()

            qs = qs.union(state_percent)
    return qs
