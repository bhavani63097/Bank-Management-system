"""
URL configuration for banking_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',views.login),
    path('dash/',views.dash,name='dash'),
    path('account/',views.accounts,name='account'),
    path('add_account/',views.add_account,name='add_account'),
    path('up_account/<int:id>',views.up_account,name='up_account'),
    path('del_account/<int:id>',views.del_account,name='del_account'),
    path('announcement/',views.announcements,name='announcement'),
    path('add_announcement/',views.add_announcement,name='add_announcement'),
    path('up_announcement/<int:id>',views.up_announcement,name='up_announcement'),
    path('del_announcement/<int:id>',views.del_announcement,name='del_announcement'),
    path('tran_admin/',views.tran_admin,name='tran_admin'),
    path('dep_admin/',views.dep_admin,name='dep_admin'),
    path('with_admin/',views.with_admin,name='with_admin'),
    path('tran_from_admin/',views.tran_from_admin,name='tran_from_admin'),
    
    
    
    
    
    path('login_user/',views.login_user),
    path('home/',views.home,name='home'),
    path('tran_user/',views.tran_user,name='tran_user'),
    path('dep_user/',views.dep_user,name='dep_user'),
    path('with_user/',views.with_user,name='with_user'),
    path('tran_from_user/',views.tran_from_user,name='tran_from_user')
    
]   
