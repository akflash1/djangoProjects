from django.contrib import admin
from .models import Article, Topic, Comment

admin.site.register(Article)
admin.site.register(Topic)
admin.site.register(Comment)
