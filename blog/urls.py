from django.urls import path,include
from . import views




urlpatterns = [
    path('',views.blog_home,name='blog_home'),
    path('manage_blogs/',views.manage_blogs,name='manage_blogs'),
    # path('sample_blog/',views.sample_blog,name='sample_blog'),

    path('create_blog/',views.create_blog,name='create_blog'),
    path('<str:pk>/',views.view_blog,name='view_blog'),
    path('update/<str:pk>/',views.update_blog,name='update_blog'),

]