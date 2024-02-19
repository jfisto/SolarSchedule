from django.contrib.auth.models import AbstractUser
from django.db import models

from solar_schedule.managers import UsersManager


class Users(AbstractUser):
    STATUS_CHOICE = [
        ('ONLINE', 'Онлайн'),
        ('OFFLINE', 'Оффлайн'),
        ('DELETE', 'Удалён'),
        ('BLOCKED', 'Заблокирован'),
    ]
    email = models.EmailField(max_length=127, blank=False, null=False, unique=True, verbose_name='Электронная почта')
    username = models.CharField(max_length=127, blank=False, null=False, unique=True, verbose_name='Имя пользователя')
    status = models.CharField(max_length=16, blank=False, null=False, verbose_name='Статус', choices=STATUS_CHOICE,
                              default='OFFLINE')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UsersManager()

    class Meta:
        ordering = ["username"]
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
