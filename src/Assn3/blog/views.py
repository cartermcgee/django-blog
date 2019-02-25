from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Blog, Comment
from django.utils import timezone


def index(request):
    latest_blog_list = Blog.objects.order_by('-pub_date_blog')[]
    return render(request, 'blog/index.html', {
        'latest_blog_list': latest_blog_list
    })

def nuke(request):
    for b in Blog.objects.all():
        b.delete()
    return HttpResponse('The database is clean')

def init(request):
    nuke(request)
    for i in range(10):
        b = Blog(title="Blog Post #" + str(i), author="John Jones", pub_date_blog=timezone.now(), blog_content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ultrices tortor sed arcu elementum tempor. Sed ullamcorper convallis placerat.")
        b.save()
        
        for j in range(3):
            c = Comment(blog=b, nickname="BlogCommentor"+str(j), email_address='emailaddress@gmail.com', pub_date_comment=timezone.now(), comment_content='Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit')
            c.save()
    return HttpResponse('The database has been initialized')