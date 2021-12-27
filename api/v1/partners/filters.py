import django_filters as filters

from partners.models import DiagnosticDepartment


class DiagnosticsListFilter(filters.FilterSet):
    region = filters.CharFilter(lookup_expr='exact')
    district = filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = DiagnosticDepartment
        fields = ['region', 'district']