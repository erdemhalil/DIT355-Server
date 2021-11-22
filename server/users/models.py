from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from django.db import models
from .user_manager import *


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    """ email acts as username in all cases """

    created_at = models.DateTimeField(auto_now_add=True)

    first_name = models.CharField(_('first name'), blank=True, max_length=150)
    last_name = models.CharField(_('last name'), blank=True, max_length=150)

    def __str__(self):
        return self.email

    USERNAME_FIELD = 'email'

    objects = UserManager()

    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
