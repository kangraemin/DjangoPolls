# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

# Project 안에는 여러개의 app 존재 가능
# {% url %} template 태그 사용 할 때 어떤 app의 view에서 url을 만들어 낼 지 알기위해 app name 사용

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]


# urlpatterns = [
#     # ex: /polls/
#     url(r'^$', views.index, name='index'),
#
#     # ?P<question_id> -> question_id라는 이름으로 뒤의 값을 받아서 넘긴다는 문법
#     #ex : /polls/숫자
#     url(r'(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#
#     # ex: /polls/숫자/results/
#     url(r'(?P<question_id>[0-9]+)/results/$',views.results, name='results'),
#
#     # ex: /polls/숫자/vote/
#     url(r'(?P<question_id>[0-9]+)/vote/$',views.vote, name='vote'),
# ]


