from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('', include('django.contrib.auth.urls')),
    #path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    
]