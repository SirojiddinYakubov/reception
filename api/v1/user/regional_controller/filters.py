import re
import datetime
import django_filters as filters
from django.db.models import Q

from application.models import (
    Application, PROCESS_CHOICES
)
from reception.settings import LOCAL_TIMEZONE


class ApplicationRightFilter(filters.FilterSet):
    old_request = filters.CharFilter(
        method='right_filter'
    )
    q = filters.CharFilter(
        method='search_filter'
    )

    order_by = filters.CharFilter(
        method='func_order_by'
    )

    def func_order_by(self, queryset, name, value):
        column = value.split(':')[0]
        dir = value.split(':')[1]
        return queryset.order_by("{0}{1}".format('-' if dir == 'desc' else '', column))

    def right_filter(self, queryset, name, value):
        qs = queryset
        if value != None:
            request = re.findall(r"\w{1,}=[\w-]{1,}", value)
            if request:
                for item in request:
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
                    if key == 'section':
                        qs = qs.filter(section__id=value)

                    if key == 'confirm':
                        qs = qs.filter(car__is_confirm=value)

                    if key == 'technical_confirm':
                        qs = qs.filter(car__is_technical_confirm=value)

                    if key == 'date':
                        today_min = datetime.datetime.now().replace(tzinfo=LOCAL_TIMEZONE, hour=0, minute=0, second=0)
                        today_max = datetime.datetime.now().replace(tzinfo=LOCAL_TIMEZONE, hour=23, minute=59, second=59)
                        some_day_last_week = (datetime.datetime.now() - datetime.timedelta(days=7)).replace(
                            tzinfo=LOCAL_TIMEZONE, hour=0,
                            minute=0, second=0)
                        some_day_last_month = datetime.datetime.now().replace(day=1, hour=0, minute=0, second=0,
                                                                     tzinfo=LOCAL_TIMEZONE)
                        some_day_last_year = datetime.datetime.now().replace(day=1, month=1, hour=0, minute=0, second=0,
                                                                    tzinfo=LOCAL_TIMEZONE)
                        if value == 'today':
                            qs = qs.filter(updated_date__range=(today_min, today_max))

                        if value == 'last-7-days':
                            qs = qs.filter(updated_date__range=(some_day_last_week, today_max))

                        if value == 'month':
                            qs = qs.filter(updated_date__range=(some_day_last_month, today_max))

                        if value == 'year':
                            qs = qs.filter(updated_date__range=(some_day_last_year, today_max))
        return qs

    def get_choices_value(self, q, choices):
        choices_list = [key for key, value in choices if re.search(q.lower(), value.lower())]
        # refund_dict = {key: value for key, value in SERVICE_CHOICES}
        return choices_list

    def search_filter(self, queryset, name, value):
        date_pattern = '^[0-9]{2}.[0-9]{2}.[0-9]{4}$'
        day_pattern = '^[0-9]{2}$|^[0-9]{2}.$'
        day_and_month_pattern = '^[0-9]{2}.[0-9]{2}$|^[0-9]{2}.[0-9]{2}.$'

        q = value.lower()
        qs = queryset.filter(
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
            Q(Q(created_date__date=datetime.datetime.strptime(q[0:10], '%d.%m.%Y').date()) | Q(
                updated_date__date=datetime.datetime.strptime(q[0:10], '%d.%m.%Y').date()) if re.match(date_pattern, q) else Q()) |
            # filter by day_pattern
            Q(Q(created_date__day=q[0:2]) | Q(updated_date__day=q[0:2]) if re.match(day_pattern, q) else Q()) |
            # filter by day_and_month_pattern
            Q(Q(Q(created_date__day=q[0:2]) & Q(created_date__month=q[3:5])) | Q(
                Q(updated_date__day=q[0:2]) & Q(updated_date__month=q[3:5])) if re.match(day_and_month_pattern,
                                                                                         q) else Q())
        )

        return qs


# class OrganizationWorkplaceListFilter(filters.FilterSet):
# department = filters.CharFilter(field_name='department__name', lookup_expr='icontains')
# position = filters.CharFilter(field_name='position__name', lookup_expr='icontains')
# employee = filters.CharFilter(method='employee_filter')
# salary_rate = filters.CharFilter(lookup_expr="icontains")

# department = filters.CharFilter(field_name='department__id', lookup_expr='icontains')
# position = filters.CharFilter(field_name='position__id', lookup_expr='icontains')
# employee = filters.CharFilter(field_name='employee__id')
# salary_rate = filters.CharFilter(lookup_expr="icontains")
#
# class Meta:
#     model = Workplace
#     fields = {
#         'salary_rate',
#     }

# def employee_filter(self, queryset, name, value):
#     values = value.split(' ')
#     qset = queryset.filter(reduce(operator.and_, (
#         Q(employee__first_name__icontains=value) | Q(employee__last_name__icontains=value) | Q(
#             employee__middle_name__icontains=value) for value in values)))
#     return qset


# class EmployeeAttestationListFilter(filters.FilterSet):
#     employee = filters.CharFilter(
#         method='employee_filter'
#     )
#     department = filters.CharFilter(field_name="employee__workplace__department__name", lookup_expr="icontains")
#     date = filters.DateFilter()
#     conclusion = filters.CharFilter(lookup_expr="iconatins")
#     is_passed = filters.CharFilter(lookup_expr='icontains')
#
#     def employee_filter(self, queryset, name, value):
#         values = value.split(' ')
#         qs = queryset.filter(reduce(operator.and_, (
#             Q(employee__first_name__icontains=value) | Q(employee__last_name__icontains=value) | Q(
#                 employee__middle_name__icontains=value) for value in values)))
#         return qs
#
#     class Meta:
#         model = EmployeeAttestation
#         fields = {
#             'date',
#             'conclusion',
#             'is_passed',
#         }
