from django.urls import path

from users.views import get_profile, MyTokenObtainPairView, get_users

app_name = 'users'

urlpatterns = [
    path('', get_users, name='get_users'),
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('profile/', get_profile, name='get_profile'),
]