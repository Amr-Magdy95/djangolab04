from django.http.response import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.decorators import permission_classes


from django.http.response import HttpResponse

from rest_framework.authtoken.models import Token

def hello_world(request):
    return HttpResponse('hello world')

@api_view(["POST"])
@permission_classes([])
def signup(request):
    data = {'data': '', 'status': ''}

    user_serialized = UserSerializer(data=request.data)

    if user_serialized.is_valid():
        user_serialized.save()
        data['data'] = {'user': user_serialized.data.get('username'), 'message': "user created", "token": Token.objects.get(user__username=user_serialized.data.get('username')).key}
        data['status']= status.HTTP_201_CREATED
    else:
        data['data'] = user_serialized.errors
        data['status']= status.HTTP_400_BAD_REQUEST
    
    return Response(**data)

@api_view(['POST'])
def logout(request):
    try:
        request.user.auth_token.delete()
    except (AttributeError):
        pass
    return Response(status=status.HTTP_200_OK)



