from django.urls import path
from .views import *

urlpatterns = [
    path('api/create_transaction/', views.create_transaction, name='create_transaction'),
    # path('api/list_transactions/', views.list_transactions, name='list_transactions'),
]











# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import FiatWalletViewSet, CryptoWalletViewSet, TransactionViewSet

# router = DefaultRouter()
# router.register(r'fiat-wallets', FiatWalletViewSet, basename='fiatwallet')
# router.register(r'crypto-wallets', CryptoWalletViewSet, basename='cryptowallet')
# router.register(r'transactions', TransactionViewSet, basename='transaction')

# urlpatterns = [
#     path('', include(router.urls)),
# ]
