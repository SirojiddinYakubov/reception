from datetime import timedelta

from django.contrib.humanize.templatetags.humanize import naturalday, intcomma
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from reception.settings import MINIMUM_BASE_WAGE
from service.models import *
from user.models import Constant


def calculation_state_duty_service_price(service):
    service = get_object_or_404(Service, id=service.id)
    car = get_object_or_404(Car, id=service.car.id)
    created_user = get_object_or_404(User, id=service.created_user.id)

    re_registration = StateDutyPercent.objects.filter(car_is_new=car.is_new,
                                                      state_duty=6).first()
    registration = StateDutyPercent.objects.filter(car_type=car.type,
                                                   lost_number=car.lost_number, is_old_number=car.is_old_number,
                                                   car_is_new=car.is_new, state_duty=5).first()
    technical_passport = StateDutyPercent.objects.filter(state_duty=4).first()
    inspection = StateDutyPercent.objects.filter(person_type=service.person_type, car_type=service.car.type,
                                                 state_duty=3).first()

    if datetime.datetime.now().date() > service.contract_date + timedelta(days=10):
        try:
            fine = StateDutyPercent.objects.filter(state_duty=7, lost_technical_passport=False).first().percent
        except AttributeError:
            fine = 0
            print("10 KUN O'TGANLIGI UCHUN JARIMA FOIZI TOPILMADI")
    else:
        fine = 0


    if car.lost_technical_passport:
        try:
            fine_lost_technical_passport = StateDutyPercent.objects.filter(state_duty=7,lost_technical_passport=car.lost_technical_passport).first().percent
            fine = fine + fine_lost_technical_passport
        except AttributeError:
            print("YO'QOLGAN TEX PASSPORT UCHUN JARIMA FOIZI TOPILMADI")


    if car.is_new:
        state_percent = StateDutyPercent.objects.filter(state_duty=1).first().percent
        road_fund = int(int(state_percent) / 100 * int(car.price))

    else:
        # ishlab chiqarilganiga 3 yil to'lmagan
        if timezone.now().year - 3 <= int(service.car.made_year):
            state_percent = StateDutyPercent.objects.filter(state_duty=2, car_type=car.type, start=0,
                                                            stop=3).first().percent
        # 3 yil to'lgan lekin 7 yil to'lmagan
        elif timezone.now().year - 3 >= int(service.car.made_year) and timezone.now().year - 7 <= int(
                service.car.made_year):
            state_percent = StateDutyPercent.objects.filter(state_duty=2, car_type=car.type, start=3,
                                                            stop=7).first().percent
        # 7 yildan ortiq
        elif timezone.now().year - 7 >= int(service.car.made_year):
            state_percent = StateDutyPercent.objects.filter(state_duty=2, car_type=car.type, start=7,
                                                            stop=0).first().percent
        else:
            state_percent = 0
            print("YO'L FONDI OT KUCHI TOPILMADI")

        road_fund = int(MINIMUM_BASE_WAGE / 100 * int(state_percent) * car.engine_power)

    context = ''
    total_prices = 0
    if re_registration:
        try:
            score = StateDutyScore.objects.filter(state_duty=re_registration.state_duty).first().score
        except AttributeError:
            score = 0
            print('QAYTA RO\'YHATLASH SCORE NOT FOUND')
        price = int(MINIMUM_BASE_WAGE / 100 * re_registration.percent)
        total_prices += price
        context += f'<hr class="line m-0 p-0">' \
                   f'<div class=\'row\'>' \
                   f'<div class=\'col-4\'>' \
                   f'<span>{re_registration.get_state_duty_display()}</span>' \
                   f'</div>' \
                   f'<div class=\'col-4 text-left\'>' \
                   f'<span>{score}</span>' \
                   f'</div>' \
                   f'<div class=\'col-4 text-right\'>' \
                   f'<span>{intcomma(price)} so\'m</span>' \
                   f'</div>' \
                   f'</div>'
    else:
        print('QAYTA RO\'YHATLASH PERCENT NOT FOUND')

    if registration:
        try:
            score = StateDutyScore.objects.filter(state_duty=registration.state_duty).first().score
        except AttributeError:
            score = 0
            print('RO\'YHATLASH SCORE NOT FOUND')

        price = int(MINIMUM_BASE_WAGE / 100 * registration.percent)
        total_prices += price
        context += f'<hr class="line m-0 p-0">' \
                   f'<div class=\'row\'>' \
                   f'<div class=\'col-4\'>' \
                   f'<span>{registration.get_state_duty_display()}</span>' \
                   f'</div>' \
                   f'<div class=\'col-4 text-left\'>' \
                   f'<span>{score}</span>' \
                   f'</div>' \
                   f'<div class=\'col-4 text-right\'>' \
                   f'<span>{intcomma(price)} so\'m</span>' \
                   f'</div>' \
                   f'</div>'
    else:
        print('RO\'YHATLASH PERCENT NOT FOUND')

    if technical_passport:
        try:
            score = StateDutyScore.objects.filter(state_duty=technical_passport.state_duty,region=created_user.region, district=created_user.district).first().score
        except AttributeError:
            score = 0
            print('QAYD ETISH GUVOHNOMASI SCORE NOT FOUND')

        price = int(MINIMUM_BASE_WAGE / 100 * technical_passport.percent)
        total_prices += price
        context += f'<hr class="line m-0 p-0">' \
                   f'<div class=\'row\'>' \
                   f'<div class=\'col-4\'>' \
                   f'<span>{technical_passport.get_state_duty_display()}</span>' \
                   f'</div>' \
                   f'<div class=\'col-4 text-left\'>' \
                   f'<span>{score}</span>' \
                   f'</div>' \
                   f'<div class=\'col-4 text-right\'>' \
                   f'<span>{intcomma(price)} so\'m</span>' \
                   f'</div>' \
                   f'</div>'
    else:
        print('QAYD ETISH GUVOHNOMASI PERCENT NOT FOUND')

    if inspection:
        try:
            score = StateDutyScore.objects.filter(state_duty=inspection.state_duty, region=created_user.region,
                                              district=created_user.district).first().score
        except AttributeError:
            score = 0
            print('TEXNIK KO\'RIK SCORE NOT FOUND')

        price = int(MINIMUM_BASE_WAGE / 100 * inspection.percent)
        total_prices += price
        context += f'<hr class="line m-0 p-0">' \
                   f'<div class=\'row\'>' \
                   f'<div class=\'col-4\'>' \
                   f'<span>{inspection.get_state_duty_display()}</span>' \
                   f'</div>' \
                   f'<div class=\'col-4 text-left\'>' \
                   f'<span>{score}</span>' \
                   f'</div>' \
                   f'<div class=\'col-4 text-right\'>' \
                   f'<span>{intcomma(price)} so\'m</span>' \
                   f'</div>' \
                   f'</div>'
    else:
        print('TEXNIK KO\'RIK PERCENT NOT FOUND')

    if fine:
        try:
            score = StateDutyScore.objects.filter(state_duty=7).first().score
        except AttributeError:
            score = 0
            print('JARIMA SCORE NOT FOUND')

        price = int(MINIMUM_BASE_WAGE / 100 * fine)
        total_prices += price
        context += f'<hr class="line m-0 p-0">' \
                   f'<div class=\'row\'>' \
                   f'<div class=\'col-4\'>' \
                   f'<span>Jarima</span>' \
                   f'</div>' \
                   f'<div class=\'col-4 text-left\'>' \
                   f'<span>{score}</span>' \
                   f'</div>' \
                   f'<div class=\'col-4 text-right\'>' \
                   f'<span>{intcomma(price)} so\'m</span>' \
                   f'</div>' \
                   f'</div>'

    else:
        print('JARIMA PERCENT NOT FOUND')

    if not road_fund == 0:
        try:
            if car.is_new:
                score = StateDutyScore.objects.filter(state_duty=1, region=created_user.region,
                                              district=created_user.district).first().score
            else:
                score = StateDutyScore.objects.filter(state_duty=2, region=created_user.region,
                                                      district=created_user.district).first().score
        except AttributeError:
            score = 0
            print('YO\'L FONDI SCORE NOT FOUND')
        total_prices += road_fund
        context += f'<hr class="line m-0 p-0">' \
                   f'<div class=\'row\'>' \
                   f'<div class=\'col-4\'>' \
                   f'<span>Yo\'l fondi</span>' \
                   f'</div>' \
                   f'<div class=\'col-4 text-left\'>' \
                   f'<span>{score}</span>' \
                   f'</div>' \
                   f'<div class=\'col-4 text-right\'>' \
                   f'<span>{intcomma(road_fund)} so\'m</span>' \
                   f'</div>' \
                   f'</div>'

    else:
        print('YO\'L FONDI PERCENT NOT FOUND')

    context += f"<hr style='margin: 0; background-color: #3e3e3e'>" \
               f"<div class='d-flex justify-content-between information'>" \
               f"<span><b>Jami to'lov</b></span>" \
               f"<span><b>{intcomma(total_prices)} so'm</b></span>" \
               f"</div>"

    return context
    # state_percents = StateDutyPercent.objects.filter(service=service.title)
    #
    # created_user = get_object_or_404(User, id=service.created_user.id)
    # context = ''
    #
    # if not state_percents.exists():
    #     print(f"DAVLAT BOJ FOIZLARI TOPILMADI")
    #     return context
    #
    # total_prices = 0
    # for percent in state_percents:
    #     state_title = percent.state_duty.title
    #
    #
    #     if state_title == "Yo'l fondi ot kuchi":
    #         #ishlab chiqarilganiga 3 yil to'lmagan
    #         if timezone.now().year - 3 <= int(service.car.made_year):
    #             print('3 yil to\'lmagan')
    #             if percent.start == 0 and percent.stop == 3:
    #                 if percent.car_type == service.car.type:
    #                     state_percent = percent.percent
    #                 else:
    #                     print(f"OT KUCHI {service.car.type} FOIZI TOPILMADI")
    #             else:
    #                 print(f"OT KUCHI 3 YIL TO'LMAGAN FOIZI TOPILMADI")
    #         # 3 yil to'lgan lekin 7 yil to'lmagan
    #         elif timezone.now().year - 3 >= int(service.car.made_year) and timezone.now().year - 7 <= int(service.car.made_year):
    #             print('3 yil to\'lgan lekin 7 yil to\'lmagan')
    #             if percent.start == 3 and percent.stop == 7:
    #                 if percent.car_type == service.car.type:
    #                     state_percent = percent.percent
    #                 else:
    #                     print(f"OT KUCHI {service.car.type} FOIZI TOPILMADI")
    #             else:
    #                 print(f"OT KUCHI 3 YIL TO'LGAN 7 YIL TO'LMAGAN FOIZI TOPILMADI")
    #         #7 yildan ortiq
    #         elif timezone.now().year - 7 >= int(service.car.made_year):
    #
    #             print('7 yildan ortiq')
    #             if percent.start == 7 and percent.stop == 0:
    #                 if percent.car_type == service.car.type:
    #                     state_percent = percent.percent
    #                 else:
    #                     print(f"OT KUCHI {service.car.type} FOIZI TOPILMADI")
    #             else:
    #                 print(f"OT KUCHI 3 YIL TO'LGAN 7 YIL TO'LMAGAN FOIZI TOPILMADI")
    #
    #     else:
    #         state_percent = percent.percent
    #
    #     try:
    #         state_score = StateDutyScore.objects.get(state_duty=percent.state_duty, region=created_user.region,
    #                                                  district=created_user.district)
    #         state_score = state_score.score
    #     except ObjectDoesNotExist:
    #         print(f"Davlat boji hisob raqami topilmadi")
    #
    #     if state_percent == 0:
    #         continue
    #
    #     try:
    #         MINIMUM_BASE_WAGE = int(Constant.objects.get(key='MINIMUM_BASE_WAGE').value)
    #         price = MINIMUM_BASE_WAGE / 100 * int(state_percent)
    #         state_price = int(price)
    #         total_prices += state_price
    #     except ObjectDoesNotExist:
    #         print(f"MINIMUM_BASE_WAGE NOT FOUND")
    #     state_percent = 0
    #     context += f'<hr class="line m-0 p-0">' \
    #                f'<div class=\'row\'>' \
    #                    f'<div class=\'col-4\'>' \
    #                        f'<span>{state_title}</span>' \
    #                    f'</div>' \
    #                    f'<div class=\'col-4 text-left\'>' \
    #                        f'<span>{state_score}</span>' \
    #                    f'</div>' \
    #                    f'<div class=\'col-4 text-right\'>' \
    #                        f'<span>{intcomma(state_price)} so\'m</span>' \
    #                    f'</div>' \
    #                f'</div>'
    #     state_score = 0
    # print(total_prices)
    # context += f"<hr style='margin: 0; background-color: #3e3e3e'>" \
    #            f"<div class='d-flex justify-content-between information'>" \
    #            f"<span><b>Jami to'lov</b></span>" \
    #            f"<span><b>{intcomma(total_prices)} so'm</b></span>" \
    #            f"</div>"
    #
    # return context
