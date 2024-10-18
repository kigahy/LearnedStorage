from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'content',
        )


class ArticleSerializer(serializers.ModelSerializer):
    class CommentDetailSetializer(serializers.ModelSerializer):
        class Meta:
            model=Comment
            fields=('id', 'content',)
    # comment_set 역참조 데이터를 override
    # 유효성 검사 대상이 아니기에 읽기 전용 옵션 작성
    # 쿼리셋이기 때문에 many옵션을 추가해야 함
    comment_set = CommentDetailSetializer(read_only=True, many=True)

    # 댓글 개수 제공을 위한 새로운 field 생성. override아님. 이름 마음대로 지정
    num_of_commnts = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    # article에 값 제공하는 목적으로 만듦
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)

    # 기존 article 데이터 값을 override
    # 그런데 기존 필드 override하면 Meta클래스의 read_only_field 사용못함
    # 기존 필드에 대해서만 적용가능하고, 이처럼 커스텀하면 안댐
    # 따라서 밑에 인자로 바꿔주어야 함
    # 모델 시리얼라이저의 read_only 값을 재설정함
    article = ArticleTitleSerializer(read_only = True)

    class Meta:
        model = Comment
        fields = '__all__'

        # 왜래키 필드를 읽기 전용 필드로 지정
        read_only_fields = ('article', )
