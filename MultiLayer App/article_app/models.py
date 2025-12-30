from django.db import models

# Create your models here.
class Articles(models.Model):
    ARTICLE_CATEGORIES = [
        ('technology', "Technology"),
        ('sports', 'Sports'),
        ('politics', 'Politics'),
        ('health', 'Health'),
        ('business', 'Business'),
        ('education', 'Education'),
        ('food', 'Food'),
        ('travel', 'Travel'),
        ('art', 'Art'),
        ('music', 'Music'),
        ('science', 'Science'),
        ('others', 'Others')
        
    ]
    
    title = models.CharField(max_length=255)
    authorName = models.CharField(max_length=50)
    short_description = models.TextField()
    articleParagrah = models.TextField(default="No content available")
    readtime = models.IntegerField(default=4)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    image= models.ImageField(upload_to='product-images/')
    published_on = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20,choices=ARTICLE_CATEGORIES)
    
    def __str__(self):
        return self.title[:15]