from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken

from .views import UserViewSet, get_id

router = DefaultRouter()
router.register('signup', UserViewSet)


urlpatterns = [
    # получение токена
    path('token/', ObtainAuthToken.as_view(), name='token'),
    # получение уникального id для анонимного пользователя
    path('get_id/', get_id, name='get_id'),
    # регистрация
    path('', include(router.urls)),
]
