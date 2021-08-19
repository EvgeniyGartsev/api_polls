from django.urls import path, include
from rest_framework.routers import DefaultRouter

from polls.views import PollViewSet, QuestionViewSet, AnswerViewSet

router = DefaultRouter()
router.register(r'polls', PollViewSet, basename='polls')
router.register(r'^polls/(?P<poll_id>\d+)/questions',
                QuestionViewSet,
                basename='questions')
router.register(r'^polls/(?P<poll_id>\d+)/answers',
                AnswerViewSet, basename='answers')

urlpatterns = [
    path('v1/auth/', include('users.urls')),
    path('v1/', include(router.urls))
]
