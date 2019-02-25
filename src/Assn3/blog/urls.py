from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
    path('/archive/', views.archive, name='archive')
    path('<int:blog_id>/entry/', views.entry, name='entry')
    path('nuke/', views.nuke, name='nuke')
    path('init/', views.init, name='init')
]