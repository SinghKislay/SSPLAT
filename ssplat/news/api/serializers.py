from rest_framework import serializers
from news.models import *

class ArticleSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleSource
        fields = ('__all__')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('__all__')

class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ('__all__')