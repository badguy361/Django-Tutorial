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
from form_test.views import here, add, menu, menu_db, meta, welcome, get_menu, comment, index, login, logout, list_restaurants, register
from django.contrib.auth import views
from django .contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'here/(?P<id>[\s\S]*)', here),
    re_path(r'(\d{1,2})/plus/(\d{1,2})', add),
    path('menu/', menu),
    path('menu_db/', menu_db),
    path('meta/', meta),
    path('welcome/', welcome),
    path('get_menu/', get_menu),
    re_path(r'get_menu/(\d{1,5})', get_menu),
    re_path(r'comment/(?P<id>\d{1,5})', comment), # ?P<關鍵字>要擷取的參數可以從URL中將要擷取的參數以關鍵字的方式取出
                                                # 例如/comment/1會將'1'給id
                                                # \d{1,5}是指1-5個數字

    # 實作內建登入認證
    path('index/', index),
    path('login/', login), # Djaongo 內建的登入登出判定(語法是固定用法)
    path('logout/', logout), # 要把login.html logged_out.html放到registration下

    # Django內建的登入認證
    path('accounts/login/', views.LoginView.as_view(), name='login'), # Djaongo 內建的登入登出判定(語法是固定用法)
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'), # 要把login.html logged_out.html放到registration下
    path('accounts/profile/', index),
    
    path('restaurants_list/', login_required(list_restaurants)), # login_required可以擋掉沒登入的使用者用url直接進去
    path('accounts/register/', register),
]
