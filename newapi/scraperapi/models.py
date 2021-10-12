from Scraper.db import models

# Create your models here.

class Author(models.Model):
    username = models.CharField(max_length= 255)
    
    
class Article(models.Model):
    title = models.CharField(max_length=255)
    source = models.ForeignKey(Author, related_name="Story", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)