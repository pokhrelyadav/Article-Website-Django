from rest_framework import serializers
from article_app.models import Articles

class ArticleSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    
    class Meta:
        model = Articles
        fields = "__all__"