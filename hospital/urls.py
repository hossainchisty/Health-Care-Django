from django.urls import path
from . import views

urlpatterns = [
    path('', views.hospitalView.as_view(), name='hospital'),
    # path('service/', views.service, name='service'),
    # path('schedule/', views.schedule, name='schedule'),

    path('doctor/', views.DoctorListView.as_view(), name='doctor_team'),

    path('contact/', views.ContactView.as_view(), name='contact'),

    # path('about/', views.about, name='about'),
    # path('testimonial/', views.testimonial, name='testimonial'),
]