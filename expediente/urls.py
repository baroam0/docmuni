"""docmuni URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from .views import certificadoedit, certificadolist, certificadonew, \
    expedienteedit, expedientelist, expedientenew, obralist, obranew, \
    obraedit


urlpatterns = [
    path('certificadoedit/<int:pk>', certificadoedit),
    path('certificadolist', certificadolist),
    path('certificadonew', certificadonew),
    path('expedienteedit/<int:pk>', expedienteedit),
    path('expedientelist', expedientelist),
    path('expedientenew', expedientenew),
    path('obraedit/<int:pk>', obraedit),
    path('obralist', obralist),
    path('obranew', obranew),
]
