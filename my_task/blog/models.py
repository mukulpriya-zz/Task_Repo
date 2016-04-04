from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Blog_Post(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
 
    def __str__(self):
        return "%s" % (self.title)
        
class Paragraph(models.Model):
    Blog_id = models.ForeignKey(Blog_Post)
    body = models.TextField()
    has_comment = models.BooleanField(default=False)

    
class Comment(models.Model):
    Paragraph_id = models.ForeignKey(Paragraph)
    body = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    
    
        
