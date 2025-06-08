from django.urls import path
from .views import UserRegistrationView, UserProfileView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


# In urls.py
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),  # Current user's profile
    path('profile/<int:pk>/', UserProfileView.as_view(), name='user-profile-detail'),  # Any profile
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
]
