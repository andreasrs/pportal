from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError
from django.core.urlresolvers import reverse

from datetime import datetime
from blog.models import Post, Comment, Message

# post list
def index(request):
    latest_post_list = __get_posts()
    return render(request, 'post/index.html', {'latest_post_list': latest_post_list})

# individual blog post
def post(request, post_id):
    post = __get_post(post_id)
    comments = __get_comments(post)
    return render(request, 'post/post.html', {'post': post, 'latest_comment_list': comments})

# comment list
def commentindex(request, post_id):

    def do_get(post, comments):
        return render(request, 'comment/index.html', {'post': post, 'latest_comment_list': comments})

    def do_post(post, comments, postData):
        comment_title = postData['commenttitle']
        comment_author = postData['commentauthor']
        comment_text = postData['commenttext']

        if comment_text:
            comment = Comment(post=post, title=comment_title, author=comment_author, body=comment_text, publish_date=datetime.now())
            comment.save()

            return HttpResponseRedirect(reverse('blog:comment', args=(post.id,comment.id)) + '#comment_' + str(comment.id))
        else:
            return do_error("Comment body must be specified")

    def do_error(error):
        return render(request, 'comment/index.html', {'post': post, 'latest_comment_list': comments, 'error_message': error})

    try:
        post = __get_post(post_id)
        comments = __get_comments(post)

        if request.POST:
            return do_post(post, comments, request.POST)
        else:
            return do_get(post, comments)

    except (MultiValueDictKeyError):
        return do_error("Comment body must be specified")

# individual comment (always viewed in post context)
def comment(request, post_id, comment_id):
    post = __get_post(post_id)
    comment = __get_comment(comment_id)
    latest_comment_list = __get_comments(post)
    return render(request, 'comment/comment.html', {'post': post, 'comment': comment, 'latest_comment_list': latest_comment_list})

# cv
def cvindex(request):
    return render(request, 'cv/index.html')

# contact
def contactindex(request):
    try:
        if request.method == 'POST':
            if request.POST['subject'] and request.POST['name'] and request.POST['email'] and request.POST['message']:
                message = Message(title=request.POST['subject'], name=request.POST['name'], email=request.POST['email'], message=request.POST['message'], publish_date=datetime.now())
                message.save()
                return render(request, 'contact/index.html', {'success_message': 'Your message has been delivered'})
            else:
                return render(request, 'contact/index.html', {'error_message': 'Could not send message. Make sure that you have provided all info.'})
        else:
            return render(request, 'contact/index.html')

    except MultiValueDictKeyError as e:
        return render(request, 'contact/index.html', {'error_message': 'Could not send message. Make sure that you have provided all info.'})

#TODO abstract away form view. model would be a good place?
def __get_post(post_id):
    return get_object_or_404(Post, pk=post_id)

def __get_posts():
    return Post.objects.order_by('-publish_date')[:5]

def __get_comment(comment_id):
    return get_object_or_404(Comment, pk=comment_id)

def __get_comments(post):
    return Comment.objects.filter(post_id=post.id).order_by('-publish_date')[:5]

