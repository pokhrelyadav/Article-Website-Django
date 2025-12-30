from django.shortcuts import render, get_object_or_404
from .models import Articles

# Create your views here.
def get_articles(req):
    articles = Articles.objects.all()
    return render(req, 'article_page.html', {"allarticles" : articles})

def get_one_article_by_id(req, id):
    article = get_object_or_404(Articles, pk=id)
    return render(req, 'article_detail.html', {"oneArticle" : article})