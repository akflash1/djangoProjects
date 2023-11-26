from rest_framework import serializers
from myapp.models import Article, Topic, Comment


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'title', 'description', 'subscribers_new']


class ArticleSerializer(serializers.ModelSerializer):
    topics = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'created', 'updated', 'author', 'topics']


class CommentSerializer(serializers.ModelSerializer):
    article = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['id', 'created', 'message', 'author', 'article']
