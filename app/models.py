from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=10000, blank=True, null=True)
    amount = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.description}: {self.amount}KZT"