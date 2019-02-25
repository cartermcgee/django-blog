from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=35)
    pub_date_blog = models.DateTimeField('date published')
    blog_content = models.CharField(max_length=6000)
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=35)
    email_address = models.EmailField()
    pub_date_comment = models.DateTimeField('date published')
    comment_content = models.CharField(max_length=200)
    