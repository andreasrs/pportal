from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>\d+)/$', views.post, name='post'), #/<postId>
    url(r'^comment/(?P<comment_id>\d+)/$', views.comment, name='comment') #/comment/<commentId>
)
