import operator
import re
from functools import reduce

import django_filters as filters
from django.db.models import Q

from user.models import User


class ApplicantsListFilter(filters.FilterSet):
    applicant = filters.CharFilter(
        method='applicant_filter'
    )

    def applicant_filter(self, queryset, name, value):
        if value:
            values = value.split(' ')
            qs = queryset.filter(reduce(operator.and_, (
                Q(first_name__icontains=value) |
                Q(last_name__icontains=value) |
                Q(middle_name__icontains=value) |
                Q(passport_seriya__icontains=value) |
                Q(passport_number__icontains=value)
                for value in values)))

            match = re.match(r"(^[a-z|A-Z]{2})([0-9]+)", value, re.I)
            if match:
                items = match.groups()
                qs = queryset.filter(reduce(operator.and_, (
                    Q(passport_seriya__icontains=value) |
                    Q(passport_number__icontains=value) for value in items)))
            return qs
        else:
            return queryset

    class Meta:
        model = User
        fields = ['applicant']