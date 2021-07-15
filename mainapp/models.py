from django.db import models
from django.contrib.auth.models import User


# Создайте свои модели здесь.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_organizer = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Status(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')

    def __str__(self):
        return self.title


class Record(models.Model):
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    phone = models.CharField(max_length=64, verbose_name='Телефон')
    description = models.TextField(verbose_name='Описание')
    status_id = models.ForeignKey(Status, verbose_name='Статус', on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserProfile, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return f'ID-{self.id};phone-{self.phone};user-{self.user_id};desc-{self.description};status-{self.status_id};'


class Template(models.Model):
    file_name = models.CharField(max_length=64, verbose_name='Название файла')
    option_one = models.CharField(max_length=64)
    option_two = models.CharField(max_length=64)
    option_three = models.CharField(max_length=64)
    option_four = models.CharField(max_length=64)
    option_five = models.CharField(max_length=64)
    user_id = models.ForeignKey(UserProfile, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}--{self.file_name}'
