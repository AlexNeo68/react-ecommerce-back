from django.urls import path

from users.views import get_profile, MyTokenObtainPairView, get_users, signup

app_name = 'users'

urlpatterns = [
    path('', get_users, name='get_users'),
    path('register/', signup, name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('profile/', get_profile, name='get_profile'),
]