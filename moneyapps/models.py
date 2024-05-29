from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
    # Ваши дополнительные поля для пользовательской модели

    class Meta:
        # Важно указать связь в обратную сторону для групп
        permissions = [
            ('view_user', 'Can view user'),
        ]

class FiatWallet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.user.username}'s Fiat Wallet"

class CryptoWallet(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=18, decimal_places=8, default=0.0)

    def __str__(self):
        return f"{self.user.username}'s Crypto Wallet"
        

class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('send', 'Send'),
        ('receive', 'Receive'),
    ]
    CURRENCY_CHOICES = [
        ('crypto', 'Crypto'),
        ('fiat', 'Fiat'),
        ('money', 'Money'),
    ]
    PAYMENT_METHOD_CHOICES = [
        ('bank', 'Bank'),
        ('wallet', 'Wallet'),
    ]

    # В этом месте исправляем ошибку, импортируя get_user_model
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    payment_method = models.CharField(max_length=6, choices=PAYMENT_METHOD_CHOICES)
    amount_fiat = models.DecimalField(max_digits=18, decimal_places=8)
    commission = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} {self.transaction_type} on {self.date}"


