"""Delivery URL Configuration

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.views.generic.base import RedirectView

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings

from manager.views import MainView, custom_handler404, custom_handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('favicon.ico', RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)),
    path('', MainView.as_view(), name="main"),
    path('delivery/', include('manager.urls'))
    ]


if settings.DEBUG:
    urlpatterns += static('favicon.ico', document_root='static/favicon.ico')


handler404 = custom_handler404
handler500 = custom_handler500