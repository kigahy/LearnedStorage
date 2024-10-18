from rest_framework import serializers
from .models import Article

# 전체 게시글의 모든 필드 가공할 클래스
class ArticleListSerializer(serializers.ModelSerializer) :
    class Meta:

        # Articld의 모델을 가공할 것
        # 전체 필드에 대하여 제공할 것
        model = Article
        fields = ('id', 'title', 'content')

class ArticleSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Article
        fields = "__all__"