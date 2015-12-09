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
from django.conf.urls import url
from adminLogin import views as aView
from sender import views as sView
from registration import views as rView

urlpatterns = [
    # ADMIN SITE
    url(r'admin/logo/$', aView.updateLogo, name = "app-admin-logo"),
    url(r'admin/lists/$', aView.manageLists, name = "app-admin-lists"),
    url(r'admin/individualList/$', aView.manageIndividualList, name = "app-admin-individual-list"),
    url(r'admin/senders/$', aView.manageSenders, name = "app-admin-senders"),
    url(r'admin/senderLists/$', aView.manageSenderLists, name = "app-admin-sender-lists"),
    url(r'admin/account/code$', aView.orgSecurityCode, name = "app-admin-security-code"),
    url(r'admin/account/$', aView.accountInfo, name = "app-admin-account"),
    url(r'admin/tokens/$', aView.addTokens, name = "app-admin-tokens"),
    url(r'admin/logout/$', aView.adminLogout, name = "app-admin-logout"),
    url(r'admin/deleteSender/$', aView.deleteSender, name = "app-admin-delete-sender"),
    url(r'admin/deleteList/$', aView.deleteList, name = "app-admin-delete-list"),
    url(r'admin/$', aView.adminLogin, name = "app-admin-login"),

    # SENDER SITE
    url(r'sender/$', sView.senderLogin, name = "app-sender-login"),
    url(r'sender/logout/$', sView.senderLogout, name = "app-sender-logout"),
    url(r'sender/msg/$', sView.sendMsg, name = "app-sender-msg"),

    # USER SITE
    url(r'^$', rView.register, name = "app-registration-register"),
    url(r'confirm/$', rView.confirm, name = "app-registration-confirm"),
    url(r'remove/$', rView.remove, name = "app-registration-remove"),

]
