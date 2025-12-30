from rest_framework.decorators import api_view
from rest_framework.response import Response

from article_app.models import Articles
from .serializers import ArticleSerializer

@api_view(['GET'])
def articles_list_api(request):
    articles = Articles.objects.all()
    serializer = ArticleSerializer(articles, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def article_detail_api(request, id):
    article= Articles.objects.get(id=id)
    serializer = ArticleSerializer(article, context={'request': request})
    return Response(serializer.data)