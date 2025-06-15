from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.contrib.auth.models import BaseUserManager as BUM
from django.db import models

from estate_agency.estate_agency_apps.common.models import BaseModel, UserRole

DEFAULT_USER_ROLE = 1
DEFAULT_USER_ADMIN_ROLE = 4
class BaseUserManager(BUM):
    def create_user(self, email, is_active=True, user_role=DEFAULT_USER_ROLE, is_admin=False, username=None,
                    name=None, surname=None, phone=None, password=None):
        if not email:
            raise ValueError("Users musr have email address")

        user = self.model(
            email=self.normalize_email(email.lower()),
            is_active=is_active,
            user_role=UserRole.objects.get(id=user_role),
            name=name,
            surname=surname,
            username=username,
            phone=phone,

        )

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=email,
            is_active=True,
            user_role=DEFAULT_USER_ADMIN_ROLE,
            password=password,
        )
        user.is_admin=True
        user.save(using=self._db)
        return user

class BaseUser(BaseModel, AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100, blank=True, null=True, default='')
    surname = models.CharField(max_length=100, blank=True, null=True, default='')
    username = models.CharField(max_length=100, blank=True, null=True, default='')
    email = models.EmailField(
        verbose_name='email_address',
        max_length=255,
        unique=True,
    )
    registration_date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=20, blank=True, null=True, default='')
    last_login_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    user_role = models.ForeignKey(UserRole, related_name='user_role', on_delete=models.CASCADE, default=4)
    user_bot_id = models.IntegerField(blank=True, null=True, default=0)
    user_bot_pass = models.CharField(max_length=100, blank=True, null=True, default='')

    groups = models.ManyToManyField(
        Group,
        verbose_name="groups",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        related_name="baseuser_set",  # Уникальное имя для обратной связи
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="user permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="baseuser_set",  # Уникальное имя для обратной связи
        related_query_name="user",
    )
    objects = BaseUserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    def is_staff(self):
        return True if self.user_role.id == 4 else False










