from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('short_title', 'long_title', 'desc', 'instruction')


@register(StateDutyPercent)
class StateDutyPercentTranslationOptions(TranslationOptions):
    fields = ('title', )
