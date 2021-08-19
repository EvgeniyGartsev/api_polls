from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from polls.models import Poll, Question, Answer
from users.models import UUIDAnonUser
from api.serializers import (
    PollSerializer, QuestionSerializer, AnswerSerializer)
from api.permissions import AdminOrReadOnly


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = (AdminOrReadOnly, )

    def get_queryset(self):
        # для админа - все опросы доступны
        # для остальных - только активные
        if self.request.user.is_superuser:
            return Poll.objects.all()
        return Poll.objects.filter(end_date=None)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (AdminOrReadOnly, )

    def get_queryset(self):
        # получим комментарии к посту
        poll_id = self.kwargs.get('poll_id')
        poll = get_object_or_404(Poll, pk=poll_id)
        return poll.questions


class AnswerViewSet(viewsets.ModelViewSet):
    """Обработка ответов пользователей.
    Можно в запросе передавать список объектов.
    При сохранении ответа в БД сохраняется либо
    id анонимного пользователя, либо пользователь."""

    serializer_class = AnswerSerializer
    permission_classes = (AllowAny, )

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Answer.objects.filter(user=self.request.user)
        if self.request.user.is_anonymous and 'HTTP_ID' in self.request.META:
            uuid = get_object_or_404(
                UUIDAnonUser, id=self.request.META['HTTP_ID'])
            return Answer.objects.filter(uuid=uuid)

    def create(self, request, *args, **kwargs):
        # меняем параметры сериализатора,
        # чтобы можно было передать список объектов
        serializer = AnswerSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        # добавляем пользователя при сохранении ответа в бд
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        # добавляем уникальный id, переданный в запросе
        # при сохранении ответа в бд
        else:
            uuid = get_object_or_404(
                UUIDAnonUser, id=self.request.META['HTTP_ID'])
            serializer.save(uuid=uuid)
