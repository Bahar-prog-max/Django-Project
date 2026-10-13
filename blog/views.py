from django.shortcuts import render
from .models import Post
from django.http import HttpResponse, Http404
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):
    pass
def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 1)
    page_number = request.GET.get('page', 3)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)
    context = {
        'posts': posts,
    }
    return render(request,'blog/list.html',context)

def post_detail(request, id):
    try:
        post = Post.published.get(id=id)

    except:
        raise Http404('NO POST FOUND !')
    context = {
            'post':post,
        }
    return render(request, 'blog/detaile.html', context)



