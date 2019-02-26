from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('archive/', views.archive, name='archive'),
    path('<int:blog_id>/entry/', views.entry, name='entry'),
    path('<int:blog_id>/comment/', views.comment, name='comment'),
    path('nuke/', views.nuke, name='nuke'),
    path('init/', views.init, name='init')
]