from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    office_location = models.CharField(max_length=100, blank=True, null=True)
    security_question = models.CharField(max_length=100, blank=True, null=True)
    two_fa = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name='clency',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='clency',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    class Meta:
        db_table = 'users'

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.full_name  # or any other logic you want
        super().save(*args, **kwargs)
