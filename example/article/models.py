from django.db import models
import datetime

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    pub_date = models.DateTimeField('date of published')
    likes = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.title
    
    
class Comment(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    pub_date= models.DateTimeField('date of comment',default=0)
    article = models.ForeignKey(Article)
    