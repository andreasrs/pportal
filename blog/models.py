import datetime
from django.utils import timezone
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=500)
    body = models.CharField(max_length=5000)
    publish_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.body
    def published_recently(self):
        return self.publish_date >= timezone.now() - datetime.timedelta(days=1)

class Comment(models.Model):
    post = models.ForeignKey(Post)
    body = models.CharField(max_length=1000)
    def __unicode__(self):
        return self.body

