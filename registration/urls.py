
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    
    
    path('signup/', views.signup, name="signup"),
    path('profil/', views.ProfileView.as_view(), name="profile"),
    path('edit/', views.edit, name="edit"),
    path('mesoffres/', views.addoffre, name="mesoffres"),
    path('modifierOffre/<str:pk>/', views.modifierOffre, name="modifierOffre"),
    path('supprimerOffre/<str:pk>/', views.deleteOffre, name="supprimerOffre"),
    path('upload/', views.upload, name="upload"),



    
]
