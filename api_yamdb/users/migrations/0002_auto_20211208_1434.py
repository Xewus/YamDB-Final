# Generated by Django 2.2.16 on 2021-12-08 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='role',
            field=models.CharField(choices=[('user', 'Пользователь'), ('moderator', 'Модератор'), ('admin', 'Администратор'), ('anonymous', 'Аноним')], default='user', max_length=30, verbose_name='Роль'),
        ),
    ]
