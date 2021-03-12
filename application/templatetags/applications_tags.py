
import datetime
from urllib.parse import urlencode

from django import template
from django.utils import timezone

register = template.Library()

@register.simple_tag
def get_service_name(object):
    try:
        if object.account_statement:
            return object.account_statement._meta.verbose_name
        elif object.gift_agreement:
            return object.gift_agreement._meta.verbose_name
        elif object.contract_of_sale:
            return object.contract_of_sale._meta.verbose_name
        else:
            return object._meta.verbose_name
    except AttributeError:
        return object

@register.simple_tag
def get_application_submitting(object):
    try:
        if object.account_statement:
            if object.account_statement.organization:
                return object.account_statement.organization
            else:
                return object.account_statement.created_user
        elif object.gift_agreement:
            if object.gift_agreement.organization:
                return object.gift_agreement.organization
            else:
                return object.gift_agreement.created_user
        elif object.contract_of_sale:
            if object.contract_of_sale.organization:
                return object.contract_of_sale.organization
            else:
                return object.contract_of_sale.created_user
        else:
            return f"Xizmat turini kiriting...."
    except AttributeError:
        return f"Xizmat turini kiriting...."


@register.simple_tag
def get_service(object):
    try:
        if object.account_statement:
            return object.account_statement
        elif object.gift_agreement:
            return object.gift_agreement
        elif object.contract_of_sale:
            return object.contract_of_sale
        else:
            return f"ERROR"
    except AttributeError:
        return f"ERROR"


@register.simple_tag(takes_context=True)
def render_widget(context, key, value):
    request = context.get('request')
    if bool(request.GET):
        print('if')
        # mavjud
        if key in request.GET:
            new_key = key
            new_value = request.GET[f'{key}']
            query_dict = request.GET.copy()
            del query_dict['person_type']

            query = '&'.join([f'{new_key}={new_value}', *['{}={}'.format(k, v) for k, v in query_dict.items()]])
            print(query)
            return query
        else:
            print('key off')
            return f"&{key}={value}"
    else:
        print('else')
        # mavjud emas
        return f"?{key}={value}"