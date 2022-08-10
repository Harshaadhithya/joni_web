from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about_us',views.about_us,name='about_us'),
    path('services',views.services_page,name='services'),
    path('services/<str:service_name>/',views.separate_service,name='separate_service'),
    path('contact_us',views.contact_us,name='contact_us'),
    path('enquiry_list',views.enquiry_list,name='enquiry_list'),
    path('update_enquiry/<str:pk>/',views.update_enquiry,name='update_enquiry'),
    path('mark_as_read/<str:pk>/',views.mark_as_read,name='mark_as_read'),
    path('manage_service',views.manage_service,name='manage_service'),
    path('add_service',views.add_service,name='add_service'),
    path('edit_service/<str:pk>/',views.edit_service,name='edit_service'),
    path('manage_testimonials',views.manage_testimonials,name='manage_testimonials'),
    path('add_testimonial',views.add_testimonial,name='add_testimonial'),
    path('edit_testimonial/<str:pk>/',views.edit_testimonial,name='edit_testimonial'),
    path('delete_testimonial/<str:pk>/',views.delete_testimonial,name='delete_testimonial'),
    path('sitemap.xml',views.sitemap,name='sitemap'),
    path('Robots.txt',views.robots,name='robots')
]