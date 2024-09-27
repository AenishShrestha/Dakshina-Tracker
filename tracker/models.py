from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Dakshina(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount} on {self.date}"