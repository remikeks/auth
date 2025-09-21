from django.urls import path
from .views import RegisterView, UserDetailView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='api-register'),
    path('login/', TokenObtainPairView.as_view(), name='api-token-obtain'),   # returns access & refresh
    path('token/refresh/', TokenRefreshView.as_view(), name='api-token-refresh'),
    path('logout/', LogoutView.as_view(), name='api-logout'),  # POST refresh token to blacklist
    path('user/', UserDetailView.as_view(), name='api-user'),
]
