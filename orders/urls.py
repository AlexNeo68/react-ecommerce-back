from django.urls import path

from orders.views import place_order, get_order, pay

app_name = 'orders'

urlpatterns = [
    path('place-order/', place_order, name='place-order'),
    path('<int:pk>/', get_order, name='get-order'),
    path('<int:pk>/pay/', pay, name='pay-order'),
]