"""LearnDjango URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from demo_app import views as demo_views

urlpatterns = [
    url(r'^$', demo_views.index),
    url(r'^index/', demo_views.index),
    url(r'^add/(\d+)/(\d+)/$', demo_views.demo_add, name="demo_add"),
    url(r'^new_add/(\d+)/(\d+)/$', demo_views.demo_add, name="new_add"),\
    # url(r'^add2/', demo_views.add2),
    url(r'^admin/', admin.site.urls),
]
