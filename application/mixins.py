import datetime
import json
import re
from rest_framework.authtoken.models import Token
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ImproperlyConfigured
from django.db.models import QuerySet, Q, Case, When, IntegerField, F
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import PermissionDenied
from application.models import *
from application.permissions import allowed_users
from reception.mixins import AllowedRolesMixin
from reception.settings import LOCAL_TIMEZONE
from service.models import *
from datetime import datetime as dt
from django.views.generic.base import *


@permission_classes([IsAuthenticated])
class ApplicationCustomMixin(ListView):
    model = Application
    request = None
    render_application_values = ['id', 'service', 'car', 'car__old_number', 'created_user',
                                 'created_date', 'process', 'file_name', 'is_payment', 'car__is_confirm',
                                 'car__is_technical_confirm', 'car__is_replace_number']

    # def __init__(self, *args, **kwargs):
    #     super(ApplicationsList, self).__init__(*args, **kwargs)

    # def get_template_names(self):
    #     print(self.request.user.role)
    #     if self.request.user.role == STATE_CONTROLLER:
    #         template_name = 'user/role/state_controller/checker_applications_list.html'
    #     elif self.request.user.role == USER:
    #         template_name = 'application/checker_applications_list.html'
    #     else:
    #         template_name = self.template_name
    #     return [template_name]

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context.update(foo='bar')
    #     context.update(object_list=self.get_queryset())
    #     return context

    # def dispatch(self, request, *args, **kwargs):
    #    self.survey = get_object_or_404(Survey, hash=self.kwargs['hash'])
    #    up = get_object_or_404(User, fk_user=self.request.user)
    #    self.client = up.fk_client
    #    if self.survey.fk_client != self.client:
    #        raise Http404
    #    return super(ApplicationCustomMixin, self).dispatch(request, *args, **kwargs)

    # @allowed_users(allowed_roles=[*allowed_roles])
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def myconverter(self, obj):
        if isinstance(obj, (datetime.datetime)):
            return obj.strftime("%d.%m.%Y %H:%M").__str__()
        elif isinstance(obj, (datetime.date)):
            return obj.strftime("%d.%m.%Y").__str__()

    def get_choices_value(self, q, choices):
        choices_list = [key for key, value in choices if re.search(q.lower(), value.lower())]
        # refund_dict = {key: value for key, value in SERVICE_CHOICES}
        return choices_list

    def get_applications_values(self, queryset):
        if self.render_application_values and queryset is not None:
            qs = queryset.values(*self.render_application_values)
            return qs
        else:
            raise Http404("get_applications_values is empty or queryset is None")

    def get_queryset(self):
        id_list = []
        qs = super().get_queryset().filter(is_active=True)

        # for item in qs:
        #     if item.section.pay_for_service and not item.is_block:
        #         id_list.append(item.id)
        #     elif not item.section.pay_for_service:
        #         id_list.append(item.id)

        # qs = super().get_queryset().filter(id__in=id_list)

        q = self.request.GET.get('q', '').lower()
        order_by = self.request.GET.get('order_by', 'created_date')
        date_pattern = '^[0-9]{2}.[0-9]{2}.[0-9]{4}$'
        day_pattern = '^[0-9]{2}$|^[0-9]{2}.$'
        day_and_month_pattern = '^[0-9]{2}.[0-9]{2}$|^[0-9]{2}.[0-9]{2}.$'

        # start right filter
        if self.request.GET.get('old_request') != None:
            old_request = re.findall(r"\w{1,}=[\w-]{1,}", self.request.GET.get('old_request'))
            if old_request:
                for item in old_request:
                    key = item.split('=')[0]
                    value = item.split('=')[1]
                    if key == 'service':
                        qs = qs.filter(service__key=value)
                    if key == 'person_type':
                        qs = qs.filter(person_type=value)
                    if key == 'process':
                        qs = qs.filter(process=value)

                    if key == 'payment':
                        qs = qs.filter(is_payment=value)

                    if key == 'confirm':
                        qs = qs.filter(car__is_confirm=value)

                    if key == 'technical_confirm':
                        qs = qs.filter(car__is_technical_confirm=value)

                    if key == 'date':

                        today_min = timezone.now().replace(tzinfo=LOCAL_TIMEZONE, hour=0, minute=0, second=0)
                        today_max = timezone.now().replace(tzinfo=LOCAL_TIMEZONE, hour=23, minute=59, second=59)
                        some_day_last_week = (timezone.now() - datetime.timedelta(days=7)).replace(
                            tzinfo=LOCAL_TIMEZONE, hour=0,
                            minute=0, second=0)
                        some_day_last_month = timezone.now().replace(day=1, hour=0, minute=0, second=0,
                                                                     tzinfo=LOCAL_TIMEZONE)
                        some_day_last_year = timezone.now().replace(day=1, month=1, hour=0, minute=0, second=0,
                                                                    tzinfo=LOCAL_TIMEZONE)
                        if value == 'today':
                            qs = qs.filter(created_date__range=(today_min, today_max))

                        if value == 'last-7-days':
                            qs = qs.filter(created_date__range=(some_day_last_week, today_max))

                        if value == 'month':
                            qs = qs.filter(created_date__range=(some_day_last_month, today_max))

                        if value == 'year':
                            qs = qs.filter(created_date__range=(some_day_last_year, today_max))

            else:
                print('not match')
        # stop right filter
        qs = qs.filter(
            Q(Q(id=q) if q.isdigit() else Q()) |
            Q(service__short_title__icontains=q) |
            Q(service__long_title__icontains=q) |
            Q(car__model__title__icontains=q) |
            Q(created_user__first_name__icontains=q) |
            Q(created_user__last_name__icontains=q) |
            Q(created_user__middle_name__icontains=q) |
            Q(car__old_number__icontains=q) |
            Q(car__given_number__icontains=q) |
            Q(car__old_technical_passport__icontains=q) |
            Q(car__given_technical_passport__icontains=q) |
            Q(car__type__title__icontains=q) |
            Q(organization__title__icontains=q) |
            Q(process__in=self.get_choices_value(q, PROCESS_CHOICES)) |
            # filter by date_pattern
            Q(Q(created_date__date=dt.strptime(q[0:10], '%d.%m.%Y').date()) if re.match(date_pattern, q) else Q()) |
            # filter by day_pattern
            Q(Q(created_date__day=q[0:2]) if re.match(day_pattern, q) else Q()) |
            # filter by day_and_month_pattern
            Q(Q(Q(created_date__day=q[0:2]) & Q(created_date__month=q[3:5])) if re.match(day_and_month_pattern,
                                                                                         q) else Q())
        ).order_by(f"-{order_by}")

        return qs

    def get_json_data(self):
        start = int(self.request.GET.get('start'))
        finish = int(self.request.GET.get('limit'))

        qs = self.get_queryset()
        data = self.get_applications_values(qs)

        list_data = []
        for index, item in enumerate(data[start:start + finish], start):
            application = get_object_or_404(self.model, id=item['id'])
            item['created_date'] = self.myconverter(item['created_date'])
            item['car'] = '<a href="{0}">{1} <br> <span style="color: black">{2}</span></a>'.format(
                reverse('user:view_car_data', kwargs={'car_id': application.car.id}),
                application.car.model.title,
                application.car.old_number if application.car.old_number else '')

            item['service'] = "<a href='{0}'>{1}</a>".format(
                reverse('application:application_detail', kwargs={'id': application.id}),
                application.service.short_title)
            item['created_user'] = "<a href='{0}'>{1}</a>".format(
                reverse('user:view_organization_data', kwargs={'id': application.organization.id}),
                application.organization.title) if application.person_type == LEGAL_PERSON and application.organization else "<a href='{0}'>{1} {2} {3}</a>".format(
                reverse('user:view_personal_data', kwargs={'id': application.created_user.id}),
                application.created_user.last_name, application.created_user.first_name,
                application.created_user.middle_name)
            list_data.append(item)

        context = {
            'length': data.count(),
            'objects': list_data
        }

        data = json.dumps(context)
        return HttpResponse(data, content_type='json')
