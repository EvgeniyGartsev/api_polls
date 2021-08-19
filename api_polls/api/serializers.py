from django.contrib.auth import get_user_model
from rest_framework import serializers

from polls.models import Poll, Question, Answer


User = get_user_model()


class QuestionSerializer(serializers.ModelSerializer):
    poll = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field='name')

    class Meta:
        model = Question
        fields = ('id', 'text', 'question_type', 'poll')


class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(data=Question.objects.all(), many=True)

    class Meta:
        model = Poll
        fields = ('id', 'name', 'start_date', 'description', 'questions')


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('question', 'answer')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # при создании пользователя кодируем пароль
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
