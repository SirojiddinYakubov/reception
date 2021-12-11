import datetime
import re

import django_filters as filters
from django.db.models import Q


class PaymentsListFilter(filters.FilterSet):
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

    def search_filter(self, queryset, name, value):
        date_pattern = '^[0-9]{2}.[0-9]{2}.[0-9]{4}$'
        day_pattern = '^[0-9]{2}$|^[0-9]{2}.$'
        day_and_month_pattern = '^[0-9]{2}.[0-9]{2}$|^[0-9]{2}.[0-9]{2}.$'

        q = value.lower()
        qs = queryset.filter(
            Q(Q(id=q) if q.isdigit() else Q()) |
            Q(Q(application__id=q) if q.isdigit() else Q()) |
            Q(application__created_user__first_name__icontains=q) |
            Q(application__created_user__last_name__icontains=q) |
            Q(application__created_user__middle_name__icontains=q) |
            Q(application__applicant__first_name__icontains=q) |
            Q(application__applicant__last_name__icontains=q) |
            Q(application__applicant__middle_name__icontains=q) |
            Q(application__section__title__icontains=q) |
            Q(amount__icontains=q) |
            Q(state_duty_score__score__icontains=q) |
            Q(transaction_id__icontains=q) |
            Q(application__service__short_title__icontains=q) |
            Q(application__service__long_title__icontains=q) |
            Q(application__created_user__district__title__icontains=q) |
            Q(application__applicant__district__title__icontains=q) |
            # filter by date_pattern
            Q(Q(created_at__date=datetime.datetime.strptime(q[0:10], '%d.%m.%Y').date()) | Q(
                updated_at__date=datetime.datetime.strptime(q[0:10], '%d.%m.%Y').date()) if re.match(date_pattern,
                                                                                                       q) else Q()) |
            # filter by day_pattern
            Q(Q(created_at__day=q[0:2]) | Q(created_at__day=q[0:2]) if re.match(day_pattern, q) else Q()) |
            # filter by day_and_month_pattern
            Q(Q(Q(created_at__day=q[0:2]) & Q(created_at__month=q[3:5])) | Q(
                Q(updated_at__day=q[0:2]) & Q(updated_at__month=q[3:5])) if re.match(day_and_month_pattern,
                                                                                         q) else Q())
        )

        return qs