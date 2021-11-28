from help.models import *
from django import template

register = template.Library()


@register.filter("get_five_articles")
def get_five_articles(queryset, sort):
    return queryset.order_by(sort)[:5]

# @register.inclusion_tag('help/home.html')
# def get_five_articles():
#     articles = HelpArticle.objects.order_by('id')[:2]
#     return {'articles': articles }
