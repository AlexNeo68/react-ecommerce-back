from django.urls import path


from .views import get_routes

app_name = 'base'


urlpatterns = [
    path("", get_routes, name="routes"),
]
