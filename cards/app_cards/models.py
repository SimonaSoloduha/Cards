from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Card(models.Model):
    series = models.CharField(max_length=100, verbose_name='Серія картки', blank=True)
    number = models.CharField(max_length=16, blank=False, verbose_name='Номер картки')
    release_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата випуску картки')
    expiration_date = models.DateTimeField(verbose_name='Дата закінчення активності картки')
    cvv = models.CharField(max_length=16, blank=True, verbose_name='CVV')
    sum_card = models.FloatField(null=True, blank=True, verbose_name='Сума')

    ACTIVE_CHOICES = [
        ("Active", 'Активована'),
        ("NotActive", 'Не активована'),
        ("Stitched", 'Прострочена'),
    ]
    activity_flag = models.CharField(max_length=10, choices=ACTIVE_CHOICES, null=True, blank=True, default="NotActive",
                                     verbose_name='Статус')

    class Meta:
        verbose_name = 'Карта'

    def __str__(self):
        return self.number