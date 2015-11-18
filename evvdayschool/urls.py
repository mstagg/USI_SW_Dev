"""evvdayschool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
#from django.contrib import admin
from adminLogin import views

urlpatterns = [
    url(r'admin/tokens/$', views.addTokens, name = "app-admin-tokens"),
    url(r'admin/account/$', views.accountInfo, name = "app-admin-account"),
    url(r'admin/logo/$', views.updateLogo, name = "app-admin-logo"),
    url(r'admin/lists/$', views.manageLists, name = "app-admin-lists"),
    url(r'admin/senders/$', views.manageSenders, name = "app-admin-senders"),
    url(r'admin/logout/$', views.adminLogout, name = "app-admin-logout"),
    url(r'admin/deleteSender/$', views.deleteSender, name = "app-admin-delete-sender"),
    url(r'admin/deleteList/$', views.deleteList, name = "app-admin-delete-list"),
    url(r'admin/$', views.adminLogin, name = "app-admin-login"),
]
