from django.conf import settings
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, DetailView

from .forms import HelpfulForm
from .models import *


class SectionsList(ListView):
    model = HelpSection
    template_name = 'help/help/home.html'

    def get_queryset(self):
        self.sections = HelpSection.objects.all()
        return self.sections

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'sections': self.sections,
        }
        return context


class SectionDetail(DetailView):
    model = HelpSection
    template_name = 'help/help/section_detail.html'
    context_object_name = 'section'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        section = HelpSection.objects.get(slug=self.kwargs['slug'], )
        context = {
            'section': section,
        }
        return super(SectionDetail, self).get_context_data(**kwargs, **context)


class HelpfulArticleSearchView(ListView):
    template_name = 'help/help/search.html'
    context_object_name = "results"

    def get_queryset(self):
        query = self.request.GET.get('q')
        return HelpArticle.objects.filter(
            Q(title__icontains=query) | Q(text__icontains=query) | Q(
                text__icontains=query))

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     article = HelpArticle.objects.filter(slug__icontains=)
    #     context = {
    #         'article': article
    #     }


class HelpArticleDetailView(DetailView):
    model = HelpArticle
    slug_field = "slug"
    template_name = 'help/help/article_detail.html'

    def get_context_data(self, **kwargs):
        slug = self.kwargs['slug']
        helpful_article = HelpArticle.objects.get(slug=slug)
        helpful_article.view += 1
        helpful_article.save()
        form = HelpfulForm()
        ip = self.request.META.get('REMOTE_ADDR')
        yes = Helpful.objects.filter(help_article=helpful_article, status=True)
        count = Helpful.objects.filter(help_article=helpful_article)
        no = Helpful.objects.filter(help_article=helpful_article, status=False)
        # count =
        helpful = Helpful.objects.filter(help_article=helpful_article, ip=ip)
        context = {
            'helpful_article': helpful_article,
            'form': form,
            'yes': yes,
            'no': no,
            'helpful': helpful

        }

        return super(HelpArticleDetailView, self).get_context_data(**kwargs, **context)


def set_helpful(request):
    form = HelpfulForm(request.POST or None)
    article = HelpArticle.objects.get(id=request.POST.get('help_article'))
    ip = request.META.get('REMOTE_ADDR')
    if request.POST:
        print(form.errors)
        form.ip = ip
        form.help_article = article
        if request.POST.get('status'):
            form.status = False
            form.save()
        elif request.POST.get('status'):
            form.status = False
            form.save()
    next = request.POST.get('next')
    return HttpResponseRedirect(next)
