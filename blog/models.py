import datetime

from django.utils import timezone
from django.db import models

# Post
class Post(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    body = models.CharField(max_length=5000)
    publish_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.body

    def published_recently(self):
        return self.publish_date <= timezone.now() and self.publish_date >= timezone.now() - datetime.timedelta(days=1)

# Comment
class Comment(models.Model):
    post = models.ForeignKey(Post)
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    publish_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.body

# Message
class Message(models.Model):
    name = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=5000)
    publish_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.message

