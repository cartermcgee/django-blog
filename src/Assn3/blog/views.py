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
        b = Blog(title="Blog Post #" + str(i), author="John Jones", pub_date_blog=timezone.now(), blog_content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ornare sapien a consequat iaculis. Aliquam tincidunt, dolor et blandit tempor, felis elit placerat leo, sit amet finibus massa sem quis nisl. Integer faucibus, diam quis vestibulum mattis, orci enim porta nisi, non convallis erat nisl eget eros. Maecenas semper interdum magna, quis consectetur libero pharetra in. Aliquam at pretium nisi. Vestibulum finibus ornare porttitor. Vestibulum lobortis leo eu condimentum pellentesque. Duis a dignissim risus. Integer sed ante quis dolor sollicitudin tempus at id massa. Vivamus scelerisque dolor tincidunt finibus imperdiet. Etiam semper sapien eget augue scelerisque aliquet. Nunc eu dolor sit amet lorem iaculis tempus. Integer ut dignissim libero. Nunc accumsan quis nibh sed imperdiet. Morbi ultrices, risus quis sagittis mattis, ipsum lorem volutpat ex, vitae tempus sem orci ut leo. Vivamus interdum elit in aliquet convallis. Fusce sed nulla a diam vestibulum malesuada non ac ligula. Aenean non mauris et dui placerat suscipit. Quisque luctus enim ac ligula lacinia cursus. Vestibulum maximus leo quis nisi volutpat, in consequat leo hendrerit. Maecenas laoreet urna diam, et fringilla nisl pretium a. Vivamus tristique fringilla pretium. Quisque non tincidunt quam. Vivamus vel urna lobortis, imperdiet velit eu, fringilla lectus. Mauris sagittis pharetra urna, et efficitur diam vulputate quis. Fusce sed tellus sit amet nisi semper scelerisque ut ut diam. Mauris tincidunt faucibus nisl ut efficitur. Etiam facilisis, leo pulvinar varius pharetra, lacus risus condimentum elit, eu faucibus magna eros in lectus. Ut justo turpis, aliquam vulputate erat et, fermentum fringilla lacus. In eget viverra mi. Duis et fermentum orci, in cursus neque. Cras quis molestie magna. Duis efficitur ligula non ex consectetur cursus non suscipit ante. Nullam auctor lacinia scelerisque. Donec lorem lorem, ornare eget massa sed, porta rhoncus dui. Integer placerat lectus dapibus consectetur volutpat. Fusce auctor metus nec lacus mollis mollis. Duis vel risus congue metus vulputate varius quis vitae quam. Cras vitae vestibulum purus. Nulla facilisis tincidunt commodo. Duis dapibus, turpis vel finibus fringilla, enim purus finibus quam, eu euismod urna mi sed diam. Nulla sed orci eget urna efficitur laoreet sed in lorem. Pellentesque ultrices nisi sed imperdiet vehicula. Fusce rhoncus iaculis justo at viverra. Sed placerat vehicula dolor. Duis lacinia risus justo, et iaculis nisi pretium sed. Vestibulum lobortis mauris accumsan sem vulputate scelerisque fringilla eget massa. Suspendisse accumsan venenatis luctus. Donec at erat et diam posuere interdum non at nulla. Praesent mattis massa at aliquet eleifend. Pellentesque varius laoreet justo ut finibus. Sed sagittis interdum condimentum. Donec vitae risus vehicula, tincidunt erat vel, tempor nulla. Quisque vehicula velit purus, in eleifend leo imperdiet vitae. Proin nunc lectus, elementum ut mi vel, efficitur ornare tortor. Quisque facilisis laoreet sapien consequat ullamcorper. Ut mollis eu odio sed ultrices. Sed dignissim quam id lacus commodo, sit amet ullamcorper risus finibus. Sed consequat vulputate ante quis condimentum. Sed iaculis ornare dictum. Nullam accumsan magna vel ex egestas accumsan. Fusce lectus sapien, luctus eu venenatis sit amet, cursus non sem. Mauris vel massa sit amet libero fermentum interdum quis tempus libero.")
        b.save()
        
        for j in range(3):
            c = Comment(blog=b, nickname="BlogCommentor"+str(j), email_address='emailaddress@gmail.com', pub_date_comment=timezone.now(), comment_content='Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit')
            c.save()
    return HttpResponseRedirect(reverse('blog:index'))