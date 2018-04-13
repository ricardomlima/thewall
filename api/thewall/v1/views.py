# api/views.py

from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse('The Wall API version 1')

def not_found(request, exception):
    """

    Handle all 404 requests

    """

    return JsonResponse({
        'status_code': 404,
        'error': 'The resource was not found'
    }, status=404)
