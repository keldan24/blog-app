from django.shortcuts import render
from django.db.models import F, Q
from . import data
from blog.models import Posts
from django.http import HttpResponse

# Create your views here.

def index(req):
    #posts = Posts.objects.all().values()
    posts = Posts.objects.all().filter(Q(author= "John") | (Q(author= "Daniel")) | (Q(views__gt= 10)))
    return render(req, "blog/index.html", {
        "posts": posts
    })

def latest(req):
    lastest_post = Posts.objects.all().order_by("-date")
    return render(req, "blog/index.html", {
        'posts': lastest_post
    })
def top(req):
    top_post = Posts.objects.all().order_by("views")
    return render(req, "blog/index.html", {
        'posts': top_post
    })


def post(req, slug):
    
    current_post = Posts.objects.get(slug= slug)
    current_post.views = current_post.views + 1
    current_post.save()
    return  render(req, "blog/post.html", {
        "post": current_post
    })

def create_post(req):
    current_post = data.post_data[0]
    post1 = Posts(title = current_post['title'], author = current_post['author'], author_img = current_post['author_img'], views = current_post['views'], content = current_post['content'])
    post1.save()
    return HttpResponse("Saved")