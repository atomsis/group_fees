from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)


class Collect(models.Model):
    class Status(models.TextChoices):
        Birthday = 'birthday', 'День рождения'
        Wedding = 'wedding', 'Свадьба'
        Anniversary = 'anniversary', 'Юбилей'
        Unknown = 'unknown','Неизвестно'

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    occasion = models.CharField(max_length=100, choices=Status.choices,default=Status.Unknown)
    description = models.TextField(blank=True)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    collected_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    contributors_count = models.PositiveIntegerField(default=0)
    cover_image = models.ImageField(upload_to='collect_covers/', null=True, blank=True)
    completion_date = models.DateTimeField(default=timezone.now,null=True)


class Contribution(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    collect = models.ForeignKey(Collect, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)


class Donation(models.Model):
    collect = models.ForeignKey(Collect, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donation_date = models.DateTimeField(auto_now_add=True)
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
