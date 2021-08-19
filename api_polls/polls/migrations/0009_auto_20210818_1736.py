# Generated by Django 2.2.10 on 2021-08-18 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20210818_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='uuid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='users.UUIDAnonUser'),
        ),
    ]
