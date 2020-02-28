from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class communities(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    creation_date = models.DateTimeField(editable=False, blank=True)

