from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from api.serializers import UserSerializer
from .models import User, UUIDAnonUser


class UserViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    "Регистрация пользователя"
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )


@api_view(['POST'])
@permission_classes([AllowAny])
def get_id(request):
    # получение уникального id для анонимного пользователя
    uuid = UUIDAnonUser.objects.create()
    return Response({
        'your id': uuid.id
    }, status=status.HTTP_201_CREATED)
