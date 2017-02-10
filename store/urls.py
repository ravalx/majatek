from django.conf.urls import url
from django.contrib import admin
from .views import CreateSt, StListView, DelSt, StcListView
from . import views
#from django.contrib.auth import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
url(r'^create-st/', CreateSt.as_view(), name='create-st'),
url(r'^delete-st/(?P<pk>\d+)/$', DelSt.as_view(), name='delete-st'),
url(r'^$', login_required(StListView.as_view(), login_url="login/"), name='list-st'),
url(r'^add-stc/(?P<nr_st>\d+)/$', views.add_stc, name='add-stc'),
#url(r'^add-stc/(?P<pk>\d+)/$', views.add_stc, name='add-stc'),
url(r'^list-stc/', StcListView.as_view(), name='list-stc')
]