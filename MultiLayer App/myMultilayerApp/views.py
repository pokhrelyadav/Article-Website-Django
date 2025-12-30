from django.shortcuts import render, get_object_or_404
from article_app.models import Articles

def home(request):
    trendingArticle = get_object_or_404(Articles, id=5)

    return render(request, 'website/index.html',{'trendingArticle': trendingArticle})