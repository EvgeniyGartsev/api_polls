# Generated by Django 2.2.10 on 2021-08-18 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20210818_1023'),
    ]

    operations = [
        migrations.CreateModel(
            name='UUID',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='end_date',
            field=models.DateField(blank=True, db_index=True, null=True, verbose_name='дата окончания'),
        ),
        migrations.AddField(
            model_name='answer',
            name='uuid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uuid', to='polls.UUID'),
        ),
    ]
