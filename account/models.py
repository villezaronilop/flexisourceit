from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.


class User(AbstractUser):
    display_name = models.CharField(_("display name"), max_length=255, blank=True)
    email = models.EmailField(_("email address"), null=True, blank=True)

    class Meta:
        db_table = "user"

    def __str__(self):
        return f"UID: {self.pk} - {self.get_username()}"