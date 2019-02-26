from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Blog, Comment
from django.utils import timezone
from django.http import Http404
from django.db.models import Count


def index(request):
    blogs = Blog.objects.annotate(number_of_comments=Count('comment'))
    latest_blog_list = Blog.objects.order_by('-pub_date_blog')[:3]
    return render(request, 'blog/index.html', {
        'latest_blog_list': latest_blog_list,
        'blogs': blogs
    })

def archive(request):
    blogs = Blog.objects.annotate(number_of_comments=Count('comment'))
    latest_blog_list = Blog.objects.order_by('-pub_date_blog')
    return render(request, 'blog/index.html', {
        'latest_blog_list': latest_blog_list,
        'blogs': blogs
    })

def entry(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/entry.html', {
        'blog': blog
    })    

def nuke(request):
    for b in Blog.objects.all():
        b.delete()
    return HttpResponseRedirect(reverse('blog:index'))

def init(request):
    nuke(request)
    for i in range(10):
        b = Blog(title="Blog Post #" + str(i), author="John Jones", pub_date_blog=timezone.now(), blog_content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ultrices tortor sed arcu elementum tempor. Sed ullamcorper convallis placerat.")
        b.save()
        
        for j in range(3):
            c = Comment(blog=b, nickname="BlogCommentor"+str(j), email_address='emailaddress@gmail.com', pub_date_comment=timezone.now(), comment_content='Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit')
            c.save()
    return HttpResponseRedirect(reverse('blog:index'))