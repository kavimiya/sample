"""sec URL Configuration

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
from secpro import views1
from time_app import views2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('love', views1.hello),
    path('gm',views1.gm),
    path('gn', views1.gn),
    path('time', views1.telltime),
    path('time', views2.tell)
    
    
]
