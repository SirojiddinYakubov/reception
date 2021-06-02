
import datetime
from urllib.parse import urlencode

from django import template
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils import timezone

from application.models import Application
from user.models import *

register = template.Library()

@register.simple_tag
def calculate_applications_count(section_id):
    try:
        section = get_object_or_404(Section, id=section_id)
        if section.parent == None:
            region = get_object_or_404(Region, id=section.region.id)
            sections = Section.objects.filter(region=region,is_active=True, parent__isnull=False)
            qs = Application.objects.filter(section__in=sections, is_active=True, is_block=False if section.pay_for_service else True)
            all = qs.count()
            process = qs.filter(process='1').count()
            success = qs.filter(process='2').count()
            cancel = qs.filter(process='3').count()
            return {
                'all': all,
                'success': success,
                'process': process,
                'cancel': cancel
            }
        else:
            print('else')
            qs = Application.objects.filter(section=section, is_active=True,is_block=False if section.pay_for_service else True)
            all = qs.count()
            process = qs.filter(process='1').count()
            success = qs.filter(process='2').count()
            cancel = qs.filter(process='3').count()
            return {
                'all': all,
                'success': success,
                'process': process,
                'cancel': cancel
            }
    except:
        return {
                'all': 0,
                'success': 0,
                'process': 0,
                'cancel': 0
            }
#
# @register.simple_tag
# def get_application_submitting(object):
#     try:
#         if object.account_statement:
#             if object.account_statement.organization:
#                 return object.account_statement.organization
#             else:
#                 return object.account_statement.created_user
#         elif object.gift_agreement:
#             if object.gift_agreement.organization:
#                 return object.gift_agreement.organization
#             else:
#                 return object.gift_agreement.created_user
#         elif object.contract_of_sale:
#             if object.contract_of_sale.organization:
#                 return object.contract_of_sale.organization
#             else:
#                 return object.contract_of_sale.created_user
#         else:
#             return f"Xizmat turini kiriting...."
#     except AttributeError:
#         return f"Xizmat turini kiriting...."
#
#
# @register.simple_tag
# def get_service(object):
#     try:
#         if object.account_statement:
#             return object.account_statement
#         elif object.gift_agreement:
#             return object.gift_agreement
#         elif object.contract_of_sale:
#             return object.contract_of_sale
#         else:
#             return f"ERROR"
#     except AttributeError:
#         return f"ERROR"
#
#
# @register.simple_tag(takes_context=True)
# def render_widget(context, key, value):
#     request = context.get('request')
#     if bool(request.GET):
#         print('if')
#         # mavjud
#         if key in request.GET:
#             new_key = key
#             new_value = request.GET[f'{key}']
#             query_dict = request.GET.copy()
#             del query_dict['person_type']
#
#             query = '&'.join([f'{new_key}={new_value}', *['{}={}'.format(k, v) for k, v in query_dict.items()]])
#             print(query)
#             return query
#         else:
#             print('key off')
#             return f"&{key}={value}"
#     else:
#         print('else')
#         # mavjud emas
#         return f"?{key}={value}"


# @register.inclusion_tag('application/application_detail_pdf.html', takes_context=True)
# def get_qrcode_image(context):
#     # request = context.get('request')
#     # url = reverse('application:qr_code_generate')
#     # print(url)
#     return None
