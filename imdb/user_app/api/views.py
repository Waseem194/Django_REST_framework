from rest_framework.decorators import api_view


@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        pass
    