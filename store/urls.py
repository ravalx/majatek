from django.conf.urls import url
from django.contrib import admin
from .views import CreateSt, StListView, DelSt, StcListView, ProductsListView
from . import views
#from django.contrib.auth import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
url(r'^create-st/', views.add_st, name='create-st'),
url(r'^delete-st/(?P<pk>\d+)/$', DelSt.as_view(), name='delete-st'),
#url(r'^$', login_required(StListView.as_view(), login_url="login/"), name='list-st'),
url(r'^$', login_required(ProductsListView.as_view(), login_url="login/"), name='products-list'),
url(r'^add-stc/(?P<nr_st>\d+)/$', views.add_stc, name='add-stc'),
#url(r'^add-stc/(?P<pk>\d+)/$', views.add_stc, name='add-stc'),
url(r'^list-stc/', login_required(StcListView.as_view(), login_url="/"), name='list-stc')
]