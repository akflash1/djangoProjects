from rest_framework import serializers
from .models import Article, Topic, Comment

class TopicSerializer(serializers.ModelSerializer):
    class Mets:
        model = Topic
        fields = ['title', ' description', 'subscribers_new']

class ArticleSerializer(serializers.ModelSerializer):
    topic = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'created', 'updated', 'author', 'topics']

class CommentSerializer(serializers.ModelSerializer):
    topic = serializers.StringRelatedField()

    model = Comment
    fields = ['created', 'message', 'author', 'article']