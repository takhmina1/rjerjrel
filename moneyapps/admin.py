from django.contrib import admin
from .models import CustomUser, FiatWallet, CryptoWallet, Transaction

admin.site.register(CustomUser)
admin.site.register(FiatWallet)
admin.site.register(CryptoWallet)
admin.site.register(Transaction)
