from django.urls import path
from . import views

urlpatterns=[
    path('login',views.signin,name='signin'),
    path('logout',views.logout_user,name='logout'),
    path('signup',views.signup,name='signup'),
    path('update_profile',views.update_profile,name='update_profile'),
    path('user_list',views.user_list,name='user_list'),
    path('give_admin_rights/<str:pk>',views.give_admin_rights,name='give_admin_rights'),
    path('remove_admin_rights/<str:pk>',views.remove_admin_rights,name='remove_admin_rights'),
    path('delete_user_profile/<str:pk>',views.delete_user_profile,name='delete_user_profile'),
]