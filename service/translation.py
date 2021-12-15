from modeltranslation.translator import register, TranslationOptions
from .models import (Service, StateDutyPercent)


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('short_title', 'long_title', 'desc', 'instruction')


@register(StateDutyPercent)
class StateDutyPercentTranslationOptions(TranslationOptions):
    fields = ('title',)
