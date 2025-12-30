from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_articles, name='get-articles'),
    path('<int:id>/',views.get_one_article_by_id, name='get-one-article-by-id')
]
