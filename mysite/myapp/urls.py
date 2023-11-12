from django.urls import path
from .views import (
    IndexView, MainPageView, AboutView, CreateView, TopicListView, SetPasswordView, SetUserDataView,
    DeactivateView, RegisterView, LoginView, LogoutView, ShowArticleView, UpdateArticleView,
    CreateArticleView, DeleteArticleView, AddCommentView, TopicsSubscribeView,
    TopicsUnsubscribeView, ProfileUsernameView, ArchiveView, ArticleListView, TopicDetailView
)

urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('create/', CreateView.as_view(), name='create'),
    path('register/', RegisterView.as_view(), name='registration'),
    path('set-password/', SetPasswordView.as_view(), name='set_password'),
    path('set-userdata/', SetUserDataView.as_view(), name='set_userdata'),
    path('article/<int:article_id>/', ShowArticleView.as_view(), name='article_detail'),
    path('article/create/', CreateArticleView.as_view(), name='create_article'),
    path('article/<int:article_id>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('article/<int:article_id>/update/', UpdateArticleView.as_view(), name='article_update'),
    path('article/<int:article_id>/delete/', DeleteArticleView.as_view(), name='article_delete'),
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('topics/', TopicListView.as_view(), name='topic_list'),
    path('topics/<int:topic>/subscribe/', TopicsSubscribeView.as_view(), name='topics_subscribe'),
    path('topics/<int:topic>/unsubscribe/', TopicsUnsubscribeView.as_view(), name='topics_unsubscribe'),
    path('profile/<str:username>/', ProfileUsernameView.as_view(), name='profile_username'),
    path('archive/<int:year>/<int:month>/', ArchiveView.as_view(), name='archive'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('topics/<int:topic_id>/', TopicDetailView.as_view(), name='topic_detail'),
]
