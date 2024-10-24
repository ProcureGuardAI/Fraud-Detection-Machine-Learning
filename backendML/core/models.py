from django.db import models
from django.utils import timezone  
from users.models import User
from django_extensions.db.models import (
    TimeStampedModel,
    TitleSlugDescriptionModel,
    ActivatorModel
)

class CoreModel(
    TimeStampedModel,
    ActivatorModel,
    TitleSlugDescriptionModel,
    models.Model
    ):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="created_%(class)s_objects")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="updated_%(class)s_objects")
    
    class Meta:
        abstract = True

    def soft_delete(self):
        self.is_active = False
        self.save()

    def restore(self):
        self.is_active = True
        self.save()

    def save(self, *args, **kwargs):
        if self.pk:
            self.updated_at = timezone.now()
        super(CoreModel, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.__class__.__name__} object ({self.id})"

class Transaction(CoreModel):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
    transaction_description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Transaction {self.id} - {self.amount} on {self.transaction_date}"
