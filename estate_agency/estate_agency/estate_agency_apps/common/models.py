from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    rgistration_date = models.DateTimeField(db_index=True, default=timezone.now)
    last_login_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class UserRole(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = 'Роль пользователя'
        verbose_name_plural = 'Роли пользователей'

    def __str__(self):
        return self.name