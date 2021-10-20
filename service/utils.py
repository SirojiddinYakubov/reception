import datetime
from datetime import timedelta

from django.contrib.humanize.templatetags.humanize import naturalday, intcomma
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from application.models import Application, ApplicationDocument
from reception.settings import MINIMUM_BASE_WAGE
from service.models import *
from user.models import Constant


# def calculation_state_duty_service_price(application):
#     application = get_object_or_404(Application, id=application.id)
#     service = get_object_or_404(Service, id=application.service.id)
#     car = get_object_or_404(Car, id=application.car.id)
#
#     created_user = get_object_or_404(User, id=application.created_user.id)
#
#     # Davlat bojlari foizlarini olish
#     re_registration = StateDutyPercent.objects.filter(car_is_new=car.is_new, state_duty=6).first()
#
#     if car.is_replace_number:
#         if not car.is_auction:
#             registration = StateDutyPercent.objects.filter(car_type=car.type,
#                                                            lost_number=car.lost_number, is_old_number=car.is_old_number,
#                                                            car_is_new=car.is_new, state_duty=5).first()
#
#         else:
#             registration = None
#     else:
#         registration = None
#
#     technical_passport = StateDutyPercent.objects.filter(state_duty=4).first()
#     inspection = StateDutyPercent.objects.filter(person_type=application.person_type, car_type=car.type,
#                                                  state_duty=3).first()
#
#     application_document = ApplicationDocument.objects.filter(application=application,
#                                                               example_document__key=service.key).last()
#
#     if application_document and application_document.contract_date:
#         if datetime.datetime.now().date() > application_document.contract_date + timedelta(days=10):
#             try:
#                 fine = StateDutyPercent.objects.filter(state_duty=7, lost_technical_passport=False).first().percent
#             except AttributeError:
#                 fine = 0
#                 print("10 KUN O'TGANLIGI UCHUN JARIMA FOIZI TOPILMADI")
#         else:
#             fine = 0
#     else:
#         fine = 0
#
#     if car.lost_technical_passport:
#         try:
#             fine_lost_technical_passport = StateDutyPercent.objects.filter(state_duty=7,
#                                                                            lost_technical_passport=car.lost_technical_passport).first().percent
#             fine = fine + fine_lost_technical_passport
#         except AttributeError:
#             print("YO'QOLGAN TEX PASSPORT UCHUN JARIMA FOIZI TOPILMADI")
#
#     some_day_3years_ago = datetime.datetime.now().date().replace(year=datetime.datetime.now().year - 3)
#     some_day_7years_ago = datetime.datetime.now().date().replace(year=datetime.datetime.now().year - 7)
#     # print(timezone.now().date())
#     # print(some_day_3years_ago)
#     # print(some_day_7years_ago)
#     if car.is_road_fund:
#         if car.is_new:
#             state_percent = StateDutyPercent.objects.filter(state_duty=1).first().percent
#             road_fund = int(int(state_percent) / 100 * int(car.price))
#         else:
#             # ishlab chiqarilganiga 3 yil to'lmagan
#             if some_day_3years_ago <= car.made_year:
#                 # print('3 yil bo\'lmagan')
#                 state_percent = StateDutyPercent.objects.filter(state_duty=2, car_type=car.type, start=0,
#                                                                 stop=3).first().percent
#             # 3 yil to'lgan lekin 7 yil to'lmagan
#             elif some_day_3years_ago >= car.made_year and some_day_7years_ago <= car.made_year:
#                 # print('3 yil bo\'lgan 7 yil bo\'lmagan')
#                 state_percent = StateDutyPercent.objects.filter(state_duty=2, car_type=car.type, start=3,
#                                                                 stop=7).first().percent
#             # 7 yildan ortiq
#             elif some_day_7years_ago >= car.made_year:
#                 # print(' 7 yildan o\'tgan')
#                 state_percent = StateDutyPercent.objects.filter(state_duty=2, car_type=car.type, start=7,
#                                                                 stop=0).first().percent
#             else:
#                 state_percent = 0
#                 print("YO'L FONDI OT KUCHI TOPILMADI")
#
#             road_fund = int(MINIMUM_BASE_WAGE / 100 * int(state_percent) * car.engine_power)
#     else:
#         road_fund = 0
#
#     # Davlat bojlari hisob raqamlarini olish
#
#     if re_registration:
#         try:
#             score = StateDutyScore.objects.filter(state_duty=re_registration.state_duty).first()
#
#         except AttributeError:
#             score = None
#             print('QAYTA RO\'YHATLASH SCORE NOT FOUND')
#
#         price = int(MINIMUM_BASE_WAGE / 100 * re_registration.percent)
#
#         state_duty = PaidStateDuty.objects.filter(title=re_registration.state_duty, service=service).first()
#         if not state_duty:
#             PaidStateDuty.objects.create(title=re_registration.state_duty, created_user=created_user, payment=price,
#                                      service=service, score=score)
#         else:
#             state_duty.payment = price
#             state_duty.score = score
#             state_duty.updated_date = timezone.now()
#             state_duty.save()
#
#
#     else:
#         print('QAYTA RO\'YHATLASH PERCENT NOT FOUND')
#
#     if registration:
#         try:
#             score = StateDutyScore.objects.filter(state_duty=registration.state_duty).first()
#
#         except AttributeError:
#             score = None
#             print('RO\'YHATLASH SCORE NOT FOUND')
#
#         price = int(MINIMUM_BASE_WAGE / 100 * registration.percent)
#
#         state_duty = PaidStateDuty.objects.filter(title=registration.state_duty, service=service).first()
#         if not state_duty:
#             PaidStateDuty.objects.create(title=registration.state_duty, created_user=created_user, payment=price,
#                                      service=service, score=score)
#         else:
#             state_duty.payment = price
#             state_duty.score = score
#             state_duty.updated_date = timezone.now()
#             state_duty.save()
#
#     else:
#         print('RO\'YHATLASH PERCENT NOT FOUND')
#
#     if technical_passport:
#         try:
#             score = StateDutyScore.objects.filter(state_duty=technical_passport.state_duty, region=created_user.region,
#                                                   district=created_user.district).first()
#         except AttributeError:
#             score = None
#             print('QAYD ETISH GUVOHNOMASI SCORE NOT FOUND')
#
#         price = int(MINIMUM_BASE_WAGE / 100 * technical_passport.percent)
#
#         state_duty = PaidStateDuty.objects.filter(title=technical_passport.state_duty, service=service).first()
#         if not state_duty:
#             if score is not None:
#                 PaidStateDuty.objects.create(title=technical_passport.state_duty, created_user=created_user, payment=price,
#                                          service=service, score=score)
#         else:
#             state_duty.payment = price
#             state_duty.score = score
#             state_duty.updated_date = timezone.now()
#             state_duty.save()
#
#     else:
#         print('QAYD ETISH GUVOHNOMASI PERCENT NOT FOUND')
#
#     if inspection:
#         try:
#             score = StateDutyScore.objects.filter(state_duty=inspection.state_duty, region=created_user.region,
#                                                   district=created_user.district).first()
#         except AttributeError:
#             score = None
#             print('TEXNIK KO\'RIK SCORE NOT FOUND')
#
#         price = int(MINIMUM_BASE_WAGE / 100 * inspection.percent)
#
#         state_duty = PaidStateDuty.objects.filter(title=inspection.state_duty, service=service).first()
#         if not state_duty:
#             if car.is_new == False:
#                 PaidStateDuty.objects.create(title=inspection.state_duty, created_user=created_user, payment=price,
#                                          service=service, score=score)
#         else:
#             state_duty.payment = price
#             state_duty.score = score
#             state_duty.updated_date = timezone.now()
#             state_duty.save()
#
#     else:
#         print('TEXNIK KO\'RIK PERCENT NOT FOUND')
#
#     if fine:
#         try:
#             score = StateDutyScore.objects.filter(state_duty=7).first()
#
#         except AttributeError:
#             score = None
#             print('JARIMA SCORE NOT FOUND')
#
#         price = int(MINIMUM_BASE_WAGE / 100 * fine)
#         state_duty = PaidStateDuty.objects.filter(title='7', service=service).first()
#         if not state_duty:
#             PaidStateDuty.objects.create(title='7', created_user=created_user, payment=price, service=service, score=score)
#         else:
#             state_duty.payment = road_fund
#             state_duty.score = score
#             state_duty.updated_date = timezone.now()
#             state_duty.save()
#     else:
#         print('JARIMA PERCENT NOT FOUND')
#
#     if not road_fund == 0:
#         try:
#             if car.is_new:
#                 score = StateDutyScore.objects.filter(state_duty=1, region=created_user.region,
#                                                       district=created_user.district).first()
#
#                 state_duty = PaidStateDuty.objects.filter(title='1', service=service).first()
#                 if not state_duty:
#                     PaidStateDuty.objects.create(title='1', created_user=created_user, payment=road_fund, service=service,
#                                              score=score)
#                 else:
#                     state_duty.payment = road_fund
#                     state_duty.score = score
#                     state_duty.updated_date = timezone.now()
#                     state_duty.save()
#
#             else:
#                 score = StateDutyScore.objects.filter(state_duty=2, region=created_user.region,
#                                                       district=created_user.district).first()
#                 state_duty = PaidStateDuty.objects.filter(title='2', service=service).first()
#                 if not state_duty:
#                     PaidStateDuty.objects.create(title='2', created_user=created_user, payment=road_fund, service=service,
#                                              score=score)
#                 else:
#                     state_duty.payment = road_fund
#                     state_duty.score = score
#                     state_duty.updated_date = timezone.now()
#                     state_duty.save()
#
#         except AttributeError:
#             print('YO\'L FONDI SCORE NOT FOUND')
#     else:
#         print('YO\'L FONDI PERCENT NOT FOUND')
