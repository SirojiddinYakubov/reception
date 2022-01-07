import django_filters as filters
from django.db.models import Q

from driver_license.models import (CallToExam)


class CallToExamSendSmsListFilter(filters.FilterSet):
    date = filters.CharFilter(method='coming_date')
    q = filters.CharFilter(method='search')


    def coming_date(self, queryset, name, value):
        return queryset.filter(coming_date__date=value)


    def search(self, queryset, name, value):
        return queryset.filter(Q(pupil__icontains=value) | Q(phone=value))

    class Meta:
        model = CallToExam
        fields = ['date', 'q']
