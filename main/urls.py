from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('offre/', views.offre, name="offre"),

    path('detailOffre/<str:pk>/', views.detailOffre, name="detailOffre"),

    
]
