# Generated by Django 2.1.5 on 2019-02-25 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=35)),
                ('pub_date_blog', models.DateTimeField(verbose_name='date published')),
                ('blog_content', models.CharField(max_length=6000)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=35)),
                ('email_address', models.EmailField(max_length=254)),
                ('pub_date_comment', models.DateTimeField(verbose_name='date published')),
                ('comment_content', models.CharField(max_length=200)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blog')),
            ],
        ),
    ]
