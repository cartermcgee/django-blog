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

def comment(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    nickname  = request.POST.get('n', '')
    email  = request.POST.get('e', '')
    comment  = request.POST.get('c', '')
    c = Comment(blog=blog, nickname=nickname, email_address=email, pub_date_comment=timezone.now(), comment_content=comment)
    c.save()
    return HttpResponseRedirect(reverse('blog:entry', args=(blog.id,)))

def nuke(request):
    for b in Blog.objects.all():
        b.delete()
    return HttpResponseRedirect(reverse('blog:index'))

def init(request):
    nuke(request)
    for i in range(10):
        b = Blog(title="Blog Post #" + str(i), author="John Jones", pub_date_blog=timezone.now(), blog_content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris aliquam diam in justo commodo sagittis. Donec finibus nisl eget mauris pellentesque sodales. Duis enim ligula, suscipit nec nibh consectetur, accumsan ullamcorper orci. Nulla volutpat neque a urna posuere, vel laoreet est placerat. Etiam mi risus, tempor vel congue eu, accumsan a sem. Nullam velit lorem, interdum a nibh in, ullamcorper faucibus diam. Etiam a eros nunc. Curabitur ut fringilla ex. Maecenas dui nisl, vulputate at vehicula eu, iaculis id odio. Fusce lacinia sodales auctor. Nulla fringilla massa et massa vehicula venenatis. Mauris vel turpis tellus. Fusce feugiat pretium mi vel ultrices. Maecenas blandit lectus efficitur odio congue, sed euismod tortor vehicula. Suspendisse potenti. Cras maximus mauris non ipsum sagittis condimentum sed sit amet nibh. In commodo vel nunc faucibus porttitor. Morbi eget consequat est, at ultrices odio. Nullam eu lacus molestie, euismod est a, luctus nulla. Aliquam erat volutpat. Nam bibendum mauris ac orci auctor, nec cursus justo tempor. Morbi dui lectus, hendrerit ac ultricies et, euismod sit amet enim. Nunc porttitor orci non felis mollis dignissim. Mauris non nisl in massa scelerisque sagittis molestie non augue. Nam lectus justo, ornare ut fringilla eu, consequat ut tortor. Etiam facilisis eget tortor non vehicula. Curabitur ac turpis libero. Pellentesque sem urna, commodo id urna id, elementum viverra neque. Proin fringilla eget ligula quis congue. Mauris mollis lorem in cursus bibendum. In ut accumsan eros. Nulla facilisi. Suspendisse sed ex non ipsum interdum tempus. Nulla vitae elit suscipit turpis consequat molestie. In vel volutpat magna. Phasellus ultricies augue quis tellus ornare condimentum. Aliquam vel neque a massa pretium mattis non sed ante. Ut id ex venenatis, lacinia leo ac, maximus diam. Integer eleifend elementum sagittis. Praesent mauris arcu, euismod eget luctus id, pellentesque quis ante. Duis nec nisl ut eros dignissim vestibulum vitae id quam. Fusce semper nibh magna, sit amet commodo mi dapibus ac. Curabitur in maximus massa. Quisque blandit blandit tellus, ut tempus nisl venenatis eget. Praesent malesuada non nisl tincidunt sagittis. Phasellus vel leo porta, consequat ipsum ut, tincidunt dui. Integer varius nulla magna, sed maximus tellus egestas at. Phasellus eget leo magna. Donec sollicitudin tincidunt leo, eu pellentesque ex. Aliquam erat volutpat. Sed quis diam et augue aliquet iaculis quis sit amet est. Aenean non consectetur urna, quis luctus nulla. Sed sem libero, lacinia et posuere ut, facilisis vel risus. Integer ultricies auctor justo, eget convallis sem fermentum at. Cras et lectus tincidunt justo condimentum varius. Aenean euismod porta feugiat. Cras viverra ut nibh porttitor pulvinar. Nunc at egestas magna. Aenean tempus diam id velit gravida sagittis. Aliquam vulputate mattis ex eu posuere. Nulla a ultricies eros. Suspendisse aliquam augue vitae metus ultrices sodales. Etiam eu molestie erat. Ut a finibus justo. Maecenas malesuada sodales ex in molestie. Donec a risus vestibulum nibh faucibus bibendum ut commodo sem. In eros elit, tincidunt nec rhoncus quis, tincidunt sed erat. Proin luctus nisl eu dolor dictum, et bibendum nibh auctor. Suspendisse accumsan sed libero in molestie. Fusce feugiat non mi.")
        b.save()
        for j in range(3):
            c = Comment(blog=b, nickname="BlogCommentor"+str(j), email_address='emailaddress@gmail.com', pub_date_comment=timezone.now(), comment_content='Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit')
            c.save()
    return HttpResponseRedirect(reverse('blog:index'))