from django.urls import path
from .views import (
    index, main_page, about, create, topic_list, set_password, set_userdata,
    deactivate, register_view, login_view, logout_view, show_article, update_article,
    create_article, delete_article, add_comment, topics_subscribe,
    topics_unsubscribe, profile_username, archive, article_list, topic_detail
)

urlpatterns = [
    path('', main_page, name='home'),
    path('about/', about, name='about'),
    path('create/', create, name='create'),
    path('register/', register_view, name='registration'),
    path('set-password/', set_password, name='set_password'),
    path('set-userdata/', set_userdata, name='set_userdata'),
    path('article/<int:article_id>/', show_article, name='article_detail'),
    path('article/create/', create_article, name='create_article'),
    path('article/<int:article_id>/comment/', add_comment, name='add_comment'),
    path('article/<int:article_id>/update/', update_article, name='article_update'),
    path('article/<int:article_id>/delete/', delete_article, name='article_delete'),
    path('articles/', article_list, name='article_list'),
    path('topics/', topic_list, name='topic_list'),
    path('topics/<int:topic>/subscribe/', topics_subscribe, name='topics_subscribe'),
    path('topics/<int:topic>/unsubscribe/', topics_unsubscribe, name='topics_unsubscribe'),
    path('profile/<str:username>/', profile_username, name='profile_username'),
    path('archive/<int:year>/<int:month>/', archive, name='archive'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('topics/<int:topic_id>/', topic_detail, name='topic_detail'),

]
