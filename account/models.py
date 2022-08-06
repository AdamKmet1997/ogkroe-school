import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings


class AccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("User must have email")
        if not username:
            raise ValueError("User must have username")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        if not email:
            raise ValueError("User must have email")
        if not username:
            raise ValueError("User must have username")
        user = self.model(
            email=self.normalize_email(email), username=username, password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    staff_code = models.CharField(max_length=200, unique=False, blank=False, default="")

    objects = AccountManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
