from django.db import models
from django.contrib.auth import get_user_model

from users.models import UUIDAnonUser

User = get_user_model()


class Poll(models.Model):
    name = models.CharField(
        verbose_name='название', max_length=200, db_index=True, unique=True)
    start_date = models.DateField(
        verbose_name='дата старта', auto_now_add=True)
    end_date = models.DateField(
        verbose_name='дата окончания', blank=True, null=True, db_index=True)
    description = models.TextField(
        verbose_name='описание', blank=True, null=True)

    class Meta:
        ordering = ('-start_date', )
        verbose_name = 'опрос'
        verbose_name_plural = 'опросы'

    def __str__(self):
        return self.name


class Question(models.Model):
    QUESTION_TYPES = [
        ('text', 'ответ с текстом'),
        ('one_choice', 'выбор одного варианта'),
        ('many_choices', 'выбор нескольких вариантов')
    ]
    text = models.TextField(verbose_name='текст вопроса', db_index=True)
    question_type = models.CharField(
        verbose_name='тип вороса', max_length=20, choices=QUESTION_TYPES)
    poll = models.ForeignKey(
        to=Poll,
        verbose_name='опрос',
        on_delete=models.CASCADE,
        related_name='questions')

    class Meta:
        ordering = ('id', )
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'

    def __str__(self):
        return self.text[:15]


class Answer(models.Model):
    question = models.ForeignKey(
        to=Question, verbose_name='вопрос', on_delete=models.CASCADE)
    answer = models.TextField(verbose_name='ответ')
    user = models.ForeignKey(
        to=User,
        verbose_name='пользователь',
        on_delete=models.CASCADE,
        related_name='answers', blank=True, null=True)
    uuid = models.ForeignKey(
        to=UUIDAnonUser, on_delete=models.CASCADE,
        related_name='answers', blank=True, null=True)
