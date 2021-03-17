from django.contrib.humanize.templatetags.humanize import naturalday, intcomma
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from service.models import *
from user.models import Constant


def calculation_state_duty_service_price(service):
    state_percents = StateDutyPercent.objects.filter(service=service.title)

    created_user = get_object_or_404(User, id=service.created_user.id)
    context = ''

    if not state_percents.exists():
        print(f"DAVLAT BOJ FOIZLARI TOPILMADI")
        return context

    total_prices = 0
    for percent in state_percents:
        state_title = percent.state_duty.title


        if state_title == "Yo'l fondi ot kuchi":
            #ishlab chiqarilganiga 3 yil to'lmagan
            if timezone.now().year - 3 <= int(service.car.made_year):
                print('3 yil to\'lmagan')
                if percent.start == 0 and percent.stop == 3:
                    if percent.car_type == service.car.type:
                        state_percent = percent.percent
                    else:
                        print(f"OT KUCHI {service.car.type} FOIZI TOPILMADI")
                else:
                    print(f"OT KUCHI 3 YIL TO'LMAGAN FOIZI TOPILMADI")
            # 3 yil to'lgan lekin 7 yil to'lmagan
            elif timezone.now().year - 3 >= int(service.car.made_year) and timezone.now().year - 7 <= int(service.car.made_year):
                print('3 yil to\'lgan lekin 7 yil to\'lmagan')
                if percent.start == 3 and percent.stop == 7:
                    if percent.car_type == service.car.type:
                        state_percent = percent.percent
                    else:
                        print(f"OT KUCHI {service.car.type} FOIZI TOPILMADI")
                else:
                    print(f"OT KUCHI 3 YIL TO'LGAN 7 YIL TO'LMAGAN FOIZI TOPILMADI")
            #7 yildan ortiq
            elif timezone.now().year - 7 >= int(service.car.made_year):
                print('7 yildan ortiq')
                if percent.start == 7 and percent.stop == 0:
                    if percent.car_type == service.car.type:
                        state_percent = percent.percent
                    else:
                        print(f"OT KUCHI {service.car.type} FOIZI TOPILMADI")
                else:
                    print(f"OT KUCHI 3 YIL TO'LGAN 7 YIL TO'LMAGAN FOIZI TOPILMADI")

        else:
            state_percent = percent.percent

        try:
            state_score = StateDutyScore.objects.get(state_duty=percent.state_duty, region=created_user.region,
                                                     district=created_user.district)
            state_score = state_score.score
        except ObjectDoesNotExist:
            print(f"Davlat boji hisob raqami topilmadi")

        if state_percent == 0:
            continue

        try:
            MINIMUM_BASE_WAGE = int(Constant.objects.get(key='MINIMUM_BASE_WAGE').value)
            price = MINIMUM_BASE_WAGE / 100 * int(state_percent)
            state_price = int(price)
            total_prices += state_price
        except ObjectDoesNotExist:
            print(f"MINIMUM_BASE_WAGE NOT FOUND")
        state_percent = 0
        context += f'<hr class="line m-0 p-0">' \
                   f'<div class=\'row\'>' \
                       f'<div class=\'col-4\'>' \
                           f'<span>{state_title}</span>' \
                       f'</div>' \
                       f'<div class=\'col-4 text-left\'>' \
                           f'<span>{state_score}</span>' \
                       f'</div>' \
                       f'<div class=\'col-4 text-right\'>' \
                           f'<span>{intcomma(state_price)} so\'m</span>' \
                       f'</div>' \
                   f'</div>'
    print(total_prices)
    context += f"<hr style='margin: 0; background-color: #3e3e3e'>" \
               f"<div class='d-flex justify-content-between information'>" \
               f"<span><b>Jami to'lov</b></span>" \
               f"<span><b>{intcomma(total_prices)} so'm</b></span>" \
               f"</div>"

    return context