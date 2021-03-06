"""majatek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls.static import  static
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from store.views import CreateSt, StListView
from django.contrib.auth import views
from login.forms import LoginForm
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'', include('login.urls')),
    url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    #url(r'^create-st/', CreateSt.as_view(), name='create-st'),
    url(r'', include('store.urls')),
    url(r'^logout/$', views.logout, {'next_page': '/login'}),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

