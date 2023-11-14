from django.urls import path, include
from rest_framework import routers

from .resources import ArticleViewSet, TopicViewSet, CommentViewSet

router = routers.SimpleRouter()

router.register(r'articles', ArticleViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
