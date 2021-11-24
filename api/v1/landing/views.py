import datetime

from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1 import permissions
from api.v1.landing import serializers
from api.v1.service.serializers import StateDutyPercentDetailSerializer
from application.models import PERSON_CHOICES
from application.utils import calculate_state_duty_percent
from service.models import StateDutyPercent, FINE, RE_REGISTRATION, REGISTRATION, TECHNICAL_PASSPORT, INSPECTION, \
    ROAD_FUND, ROAD_FUND_HORSE_POWER, Service
from user.models import CarType


class Calculate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = serializers.CalculateSerializer(data=request.data)
        if serializer.is_valid():
            service_id = serializer.data.get('service')
            service = Service.objects.get(id=service_id)
            if service.key == 'account_statement':
                is_new = True
            else:
                is_new = False

            type = serializer.data.get('type')
            is_local = serializer.data.get('is_local')
            person_type = serializer.data.get('person_type')
            engine_power = serializer.data.get('engine_power')
            price = serializer.data.get('price')
            made_year = serializer.data.get('made_year')
            if made_year:
                made_year = datetime.datetime.strptime(made_year, '%Y-%m-%d').date()
            contract_date = serializer.data.get('contract_date')
            if contract_date:
                contract_date = datetime.datetime.strptime(contract_date, '%Y-%m-%d').date()
            is_auction = serializer.data.get('is_auction')
            save_old_number = serializer.data.get('save_old_number')
            is_saved_number = serializer.data.get('is_saved_number')
            lost_number = serializer.data.get('lost_number')
            is_old_number = serializer.data.get('is_old_number')
            is_relative = serializer.data.get('is_relative')
            lost_technical_passport = serializer.data.get('lost_technical_passport')

            qs = StateDutyPercent.objects.none()

            try:
                """Jarima"""
                if contract_date:
                    last_day_without_fine = contract_date + datetime.timedelta(days=10)

                    if last_day_without_fine.weekday() == 6:
                        last_day_without_fine = last_day_without_fine + datetime.timedelta(days=1)

                    if datetime.datetime.now().date() > last_day_without_fine:
                        """Shartnoma tuzilgan sana 10 kundan kechikganligi uchun jarima"""
                        fine1 = StateDutyPercent.objects.filter(service=service, state_duty=FINE,
                                                                contract_fine=True)
                    else:
                        fine1 = StateDutyPercent.objects.none()
                else:
                    fine1 = StateDutyPercent.objects.none()

                """Qayd etish guvohnomasi yo'qolgan yoki yo'qolmaganligidan kelib chiqib jarima"""
                fine2 = StateDutyPercent.objects.filter(service=service, state_duty=FINE,
                                                        lost_technical_passport=lost_technical_passport, lost_number=False, contract_fine=False)
                """Raqam yo'qolganligi uchun jarima"""
                fine3 = StateDutyPercent.objects.filter(service=service, state_duty=FINE,
                                                      lost_number=lost_number, lost_technical_passport=False,contract_fine=False)

                """Uchala jarimani birlashtirish"""
                qs = (fine1 | fine2 | fine3).distinct()

                """Qayta ro'yhatlash"""
                re_registration = StateDutyPercent.objects.filter(service=service, state_duty=RE_REGISTRATION)
                qs = qs.union(re_registration)

                """Ro'yhatlash ya'ni DRB uchun to'lov"""
                if not is_auction:
                    if save_old_number:
                        registration = StateDutyPercent.objects.filter(service=service, car_type=type,
                                                                       lost_number=False, is_old_number=is_old_number,
                                                                       is_auction=False,
                                                                       car_is_new=False,
                                                                       is_relative=is_relative,
                                                                       is_save_old_number=save_old_number,
                                                                       is_saved_number=is_saved_number,
                                                                       state_duty=REGISTRATION, )

                    else:
                        registration = StateDutyPercent.objects.filter(service=service, car_type=type,
                                                                       lost_number=lost_number,
                                                                       is_old_number=is_old_number,
                                                                       is_auction=False,
                                                                       car_is_new=is_new,
                                                                       is_relative=is_relative,
                                                                       is_save_old_number=save_old_number,
                                                                       is_saved_number=is_saved_number,
                                                                       state_duty=REGISTRATION)
                else:
                    registration = StateDutyPercent.objects.filter(service=service, car_type=type,
                                                                   lost_number=lost_number,
                                                                   is_old_number=is_old_number,
                                                                   car_is_new=is_new, is_auction=is_auction,
                                                                   is_save_old_number=save_old_number,
                                                                   is_saved_number=is_saved_number,
                                                                   is_relative=is_relative,
                                                                   state_duty=REGISTRATION)
                qs = qs.union(registration)

                """Yangi qayd etish guvohnomasi"""
                technical_passport = StateDutyPercent.objects.filter(state_duty=TECHNICAL_PASSPORT)
                qs = qs.union(technical_passport)

                """Texnik ko'rik"""
                if not is_new:
                    inspection = StateDutyPercent.objects.filter(service=service,
                                                                 person_type=person_type,
                                                                 car_type=type,
                                                                 state_duty=INSPECTION)
                    qs = qs.union(inspection)

                """Yo'l fondi"""
                some_day_3years_ago = datetime.datetime.now().date().replace(year=datetime.datetime.now().year - 3)
                some_day_7years_ago = datetime.datetime.now().date().replace(year=datetime.datetime.now().year - 7)

                if is_new and is_local:
                    """Yangi va mahalliy avtomobil"""
                    if made_year < datetime.datetime.strptime('25.12.2020', '%d.%m.%Y').date():
                        state_percent = StateDutyPercent.objects.filter(service=service, state_duty=ROAD_FUND)
                    else:
                        state_percent = StateDutyPercent.objects.none()
                elif is_new and not is_local:
                    """Yangi lekin mahalliy bo'lmagan avtomobil"""
                    state_percent = StateDutyPercent.objects.filter(state_duty=ROAD_FUND, service=service)
                else:
                    # ishlab chiqarilganiga 3 yil to'lmagan
                    if some_day_3years_ago <= made_year:
                        # print('3 yil bo\'lmagan')
                        state_percent = StateDutyPercent.objects.filter(service=service,
                                                                        state_duty=ROAD_FUND_HORSE_POWER, car_type=type,
                                                                        start=0,
                                                                        stop=3)
                    # 3 yil to'lgan lekin 7 yil to'lmagan
                    elif some_day_3years_ago >= made_year and some_day_7years_ago <= made_year:
                        # print('3 yil bo\'lgan 7 yil bo\'lmagan')
                        state_percent = StateDutyPercent.objects.filter(service=service,
                                                                        state_duty=ROAD_FUND_HORSE_POWER, car_type=type,
                                                                        start=3,
                                                                        stop=7)
                    # 7 yildan ortiq
                    elif some_day_7years_ago >= made_year:
                        # print(' 7 yildan o\'tgan')
                        state_percent = StateDutyPercent.objects.filter(service=service,
                                                                        state_duty=ROAD_FUND_HORSE_POWER, car_type=type,
                                                                        start=7,
                                                                        stop=0)
                    else:
                        state_percent = StateDutyPercent.objects.none()

                    if is_relative:
                        state_percent = StateDutyPercent.objects.none()

                qs = qs.union(state_percent)


            except Exception as e:
                print(e)

            state_duty_percent_serializer = StateDutyPercentDetailSerializer(qs, many=True,
                                                                             context={'engine_power': engine_power,
                                                                                      'price': price})
            return Response(state_duty_percent_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
