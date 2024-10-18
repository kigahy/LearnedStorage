from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_object_or_404

from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(
            article, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    # 쿼리셋 데이터 넣어줌
    serializer = CommentSerializer(comments, many=True)
    # 가공된 데이터 안 실제 값에 접근
    return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # 단일 댓글 조회
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'GET':
        # 단일 댓글 직렬화
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE' :
        comment.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT' :
        serializer = CommentSerializer(comment, data = request.data)
        if serializer.is_valid(raise_exception = True):

            # 이미 키 가지고 있기 때문에 인자 안넣음
            serializer.save()
            return Response(serializer.data)

@api_view(['POST'])
def comment_create(request, article_pk):
    # 게시글 조회. 어떤 게시글에 작성된 댓글인지 알아야 함
    article = Article.objects.get(pk=article_pk)
    # 사용자 입력 데이터를 직렬화(사용자가 입력한 댓글 데이터)
    # 사용자는 댓글 데이터만 쓸 뿐, 왜래키가 없음
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception = True):
        # 왜래키 데이터 입력 후 저장
        # 댓글 데이터에 딸려오는게 아니라서 따로 저장해주는 것
        # 인자 왼쪽은 필드명, 오른쪽은 변수명
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)