"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from . import view,testdb
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', view.index),
    url(r'^index/$', view.index),
    url(r'^accounts/login/$', view.index),

    url(r'^hello$', view.hello),
    url(r'^hello$', view.helloTest),
    url(r'^testdb$', testdb.testdbAdd),
    url(r'^index$', view.index),
    url(r'^base', view.base),
    url(r'^login_action/$', view.login_action),
    url(r'^event_manage/$', view.event_manage),
]
