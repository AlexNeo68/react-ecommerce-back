from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_routes(request):
    routes = [
        '/api/products/',
    ]
    return Response(routes)
