"""form_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path
from form_test.views import here, add, menu, menu_db

urlpatterns = [
    path('admin/', admin.site.urls),
    path('here/', here),
    re_path(r'(\d{1,2})/plus/(\d{1,2})', add),
    path('menu/', menu),
    path('menu_db/', menu_db),
]
