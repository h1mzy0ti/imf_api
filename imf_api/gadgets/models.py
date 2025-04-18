import uuid
from django.db import models
from django.contrib.auth.models import User
class Gadget(models.Model):
    STATUS_CHOICES = [
        ("Available", "Available"),
        ("Deployed", "Deployed"),
        ("Destroyed", "Destroyed"),
        ("Decommissioned", "Decommissioned"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gadgets',null=True, blank=True)
    codename = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Available")
    decommissioned_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.codename
