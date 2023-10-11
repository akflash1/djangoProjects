from django.urls import path
from .views import (index, main_page, about, create, topics, set_password, set_userdata, deactivate, register, login, logout, show_article, update_article, create_article, delete_article, add_comment, topics_subscribe, topics_unsubscribe, profile_username, archive)

urlpatterns = [

    path('', index, name='index'),
    path('about/', about, name='about'),
    path('create/', create, name='create'),
    path('register/', register, name='registration'),
    path('set-password/', set_password, name='set_password'),
    path('set-userdata/', set_userdata, name='set_userdata'),
    path('<int:article_id>/', show_article, name='article_detail'),
    path('create/', create_article, name='create_article'),
    path('<int:article_id>/comment/', add_comment, name='add_comment'),
    path('<int:article_id>/update/', update_article, name='article_update'),
    path('<int:article_id>/delete/', delete_article, name='article_delete'),
    path('topics/', topics, name='topics'),
    path('topics/<int:topic>/subscribe/', topics_subscribe, name='topics_subscribe'),
    path('topics/<int:topic>/unsubscribe/', topics_unsubscribe, name='topics_unsubscribe'),
    path('profile/<str:username>/', profile_username, name='profile_username'),
    path('archive/<int:year>/<int:month>/', archive, name='archive'),
    path('login/', login, name='login'),
    path('', main_page, name='home'),
]
