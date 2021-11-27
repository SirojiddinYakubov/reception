from django.urls import path

from . import views

urlpatterns = [
    path('', views.SectionsList.as_view(), name='sections_list_url'),
    path('section/<slug:slug>', views.SectionDetail.as_view(), name='section_detail_url'),
    path('search/', views.HelpfulArticleSearchView.as_view(), name='search'),

    path('detail/<slug>', views.HelpArticleDetailView.as_view(), name='article_detail_url'),
    path('set-helpful/', views.set_helpful, name='set_helpful'),
]
