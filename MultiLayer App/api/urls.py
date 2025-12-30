from django.urls import path
from . import views

urlpatterns = [
    path('articles/',views.articles_list_api,name='get-articles-api'),
    path('articles/<int:id>/',views.article_detail_api,name='article-detail-api'),
]
