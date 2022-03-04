import datetime
import re

import django_filters as filters
from django.db.models import Q

class StateDutiesReportFilter(filters.FilterSet):
    start_date = filters.DateFilter()
    end_date = filters.DateFilter()
    # section = filters.