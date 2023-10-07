"""
URL configuration for myblogproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .views import (
    main_page,
    about,
    create,
    topics,
    set_password,
    set_userdata,
    deactivate,
    register,
    login,
    logout,
    article_show,
    article_update,
    article_delete,
    article_comment,
    topics_subscribe,
    topics_unsubscribe,
    profile_username,
    archive
)


urlpatterns = [
    path('', main_page, name='main_page'),
    path('about/', about, name='about'),
    path('create/', create, name='create'),
    path('set-password/', set_password, name='set-password'),
    path('set-userdata/', set_userdata, name='set-userdata'),
    path('<int:article>/', article_show, name='article'),
    path('<int:article>/comment/', article_comment, name='article-comment'),
    path('<int:article>/delete/', article_delete, name='article-delete'),
    path('<int:article>/update/', article_update, name='article-update'),
    path('topics/', topics, name='topics'),
    path('topics/<int:topic>/subscribe/', topics_subscribe, name='topics-subscribe'),
    path('topics/<int:topic>/unsubscribe/', topics_unsubscribe, name='topics-unsubscribe'),
    path('profile/<str:username>/', profile_username, name='profile-username'),
    path('archive/<int:year>/<int:month>/', archive, name='archive'),
]