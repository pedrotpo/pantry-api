from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone

from .managers import UserProfileManager


# Base model fields
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Changing the default user model to use email as pk"""

    email = models.EmailField(db_index=True, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        if not self.first_name and not self.last_name:
            return self.email
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()
