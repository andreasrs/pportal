from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Index view")

def post(request, postId):
    return HttpResponse("A post: %s" % postId)

def comment(request, commentId):
    return HttpResponse("A comment: %s" % commentId)
