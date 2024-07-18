from datetime import datetime

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from base.models import Order, ShippingAddress, OrderItem, Product
from orders.serializers import OrderSerializer, OrderItemSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def place_order(request):
    user = request.user
    data = request.data

    order_items = data['orderItems']
    if order_items and len(order_items) == 0:
        return Response({'detail': 'Order Item is empty'}, status=status.HTTP_400_BAD_REQUEST)
    else:

        order = Order.objects.create(
            user=user,
            paymentMethod=data['paymentMethod'],
            taxPrice=data['taxPrice'],
            shippingPrice=data['shippingPrice'],
            totalPrice=data['totalPrice'],
        )

        ShippingAddress.objects.create(
            order=order,
            address=data['shippingAddress']['address'],
            city=data['shippingAddress']['city'],
            postalCode=data['shippingAddress']['postalCode'],
            country=data['shippingAddress']['country'],
            shippingPrice=data['shippingPrice'],
        )

        for item in order_items:
            product = Product.objects.get(pk=item['_id'])
            OrderItem.objects.create(
                order=order,
                product=product,
                name=product.name,
                qty=item['qty'],
                price=product.price,
                image=product.image.url
            )
            product.countInStock -= item['qty']
            product.save()

        order_serializer = OrderSerializer(order, many=False)
        return Response(order_serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_order(request, pk):
    user = request.user
    try:
        order = Order.objects.get(pk=pk)
        if user.is_staff or user == order.user:
            serializer = OrderSerializer(order, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Not authorized'}, status=status.HTTP_401_UNAUTHORIZED)
    except:
        return Response({'detail': 'Order does not exist'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def pay(request, pk):
    order = Order.objects.get(_id=pk)
    order.isPaid = True
    order.paidAt = datetime.now()
    order.save()
    return Response('Order paid', status=status.HTTP_202_ACCEPTED)