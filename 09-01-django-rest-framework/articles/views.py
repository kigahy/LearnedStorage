from rest_framework.response import Response
from rest_framework.decorators import api_view
# 대표적인 응답 상태코드가 있음
from rest_framework import status
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET' :
        articles = Article.objects.all()

        # 위 쿼리셋을 변환하기 쉬운 포맷으로 변환(직렬화)
        # 다중 데이터일 경우 many = True 추가
        serializer = ArticleListSerializer(articles, many = True)
        return Response(serializer.data)
    
    # 조건 4가지가 되었기 때문에 else 아닌 elif로 명시해줌
    elif request.method == 'POST' :

        # 모델시리얼라이저 사용하여 사용자 입력 데이터 받아 직렬화 진행
        serializer = ArticleSerializer(data = request.data)

        # 가공 끝났으니 유효성 검사 진행
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            # 저장 성공 후 201 응답 상태코드 반환
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        # 유효성 검사 실패 후 401 응답 상태코드 반환
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    if request.method == 'GET' :
        serializer = ArticleListSerializer(article)
        return Response(serializer.data)
    
    # 삭제 과정에서는 직렬화 과정 필요 없음
    elif request.method == 'DELETE' :
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT' :
        # 기존 데이터, 새로운 데이터, partial 3가지 인자 필요
        serializer = ArticleSerializer(article, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        