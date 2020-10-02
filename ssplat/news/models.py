from django.db import models

# Create your models here.


class ArticleSource(models.Model):
    source_id = models.CharField(max_length=50)
    source_name = models.CharField(max_length=50)

class Author(models.Model):
    author_name = models.CharField(max_length=100, null=True, blank=True)


class Articles(models.Model):
    source = models.ForeignKey(ArticleSource, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    Desc = models.CharField(max_length=1000, null=True, blank=True)
    url = models.CharField(max_length=1000, null=True, blank=True)
    url_image = models.CharField(max_length=1000, null=True, blank=True)
    date = models.DateTimeField(null=True)
    content = models.CharField(max_length=10000, null=True, blank=True)

print("Json parsed and Database populated!")