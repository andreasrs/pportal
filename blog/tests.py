from django.test import TestCase
from django.utils import timezone
from blog.models import Post, Comment
import datetime

class BlogTest(TestCase):
    def test_create_post(self):
        post = Post(title="Testtitle", description="test description", body="test body", publish_date=timezone.now())

    def test_create_comment(self):
        comment = Comment(post_id=1, body="test body", publish_date=timezone.now())

    def test_future_post_not_published(self):
        future = timezone.now() + datetime.timedelta(days=3)
        post = Post(title="Testtitle", description="test description", body="test body", publish_date=future)
        self.assertEquals(post.published_recently(), False)

