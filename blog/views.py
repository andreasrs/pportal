from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from blog.models import Post

def index(request):
    latest_post_list = Post.objects.order_by('-publish_date')[:5]
    return render(request, 'post/index.html', {'latest_post_list': latest_post_list})

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post/post.html', {'post': post})

def comment(request, comment_id):
    return HttpResponse("A comment: %s" % commentId)
