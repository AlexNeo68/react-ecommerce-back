from django.urls import path

from orders.views import place_order, get_order, pay, get_my_orders

app_name = 'orders'

urlpatterns = [
    path('my/', get_my_orders, name='my-orders'),
    path('place-order/', place_order, name='place-order'),
    path('<int:pk>/', get_order, name='get-order'),
    path('<int:pk>/pay/', pay, name='pay-order'),
]