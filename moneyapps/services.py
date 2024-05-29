import httpx
from decimal import Decimal
from django.utils import timezone
from .models import FiatWallet, CryptoWallet, Transaction

# COINGECKO_API_URL = "https://api.binance.com/api/v3/ticker/bookTicker"
# OPENEXCHANGERATES_API_URL = "https://console.fastforex.io/"
# OPENEXCHANGERATES_API_KEY = "xrQq7XzYLGGXvK2ci0X9jhUKRJMvxnFBS9GiLnMAffb77394"  



# async def get_crypto_rate(crypto: str, fiat: str) -> Decimal:
#     params = {
#         'ids': crypto,
#         'vs_currencies': fiat
#     }
#     async with httpx.AsyncClient() as client:
#         response = await client.get(COINGECKO_API_URL, params=params)
#         response.raise_for_status()
#         data = response.json()
#         return Decimal(data[crypto][fiat])
#     return data


# async def get_fiat_rate(base: str, target: str) -> Decimal:
#     params = {
#         'app_id': OPENEXCHANGERATES_API_KEY,
#         'base': base
#     }
#     async with httpx.AsyncClient() as client:
#         response = await client.get(OPENEXCHANGERATES_API_URL, params=params)
#         response.raise_for_status()
#         data = response.json()
#         return Decimal(data['rates'][target])
#     return data


    

# async def get_combined_rate(crypto: str, fiat: str) -> Decimal:
#     crypto_to_usd = await get_crypto_rate(crypto, 'usd')
#     usd_to_fiat = await get_fiat_rate('USD', fiat)
#     return crypto_to_usd * usd_to_fiat
  



# async def perform_transaction(user, transaction_type, amount_fiat, amount_crypto):
#     fiat_wallet = FiatWallet.objects.get(user=user)
#     crypto_wallet = CryptoWallet.objects.get(user=user)

#     if transaction_type == 'buy':
#         fiat_wallet.balance -= amount_fiat
#         crypto_wallet.balance += amount_crypto
#     elif transaction_type == 'sell':
#         fiat_wallet.balance += amount_fiat
#         crypto_wallet.balance -= amount_crypto

#     fiat_wallet.save()
#     crypto_wallet.save()

    
# ''''''''''''''''''''''''''''''


# # import httpx

# # async def get_exchange_rate_api1(from_currency, to_currency):
# #     async with httpx.AsyncClient() as client:
# #         response = await client.get(f'https://api.binance.com/api/v3/ticker/bookTicker{from_currency}')
# #         response.raise_for_status()
# #         rates = response.json().get('rates', {})
# #         return rates.get(to_currency)

# # async def get_exchange_rate_api2(from_currency, to_currency):
# #     async with httpx.AsyncClient() as client:
# #         response = await client.get(f'https://console.fastforex.io/{from_currency}')
# #         response.raise_for_status()
# #         rates = response.json().get('rates', {})
# #         return rates.get(to_currency)

# # async def get_exchange_rate(from_currency, to_currency, api_choice='api1'):
# #     if api_choice == 'api1':
# #         return await get_exchange_rate_api1(from_currency, to_currency)
# #     elif api_choice == 'api2':
# #         return await get_exchange_rate_api2(from_currency, to_currency)
# #     else:
# #         raise ValueError("Invalid API choice")

# # def calculate_received_amount(amount, exchange_rate, commission_rate=0.01):
# #     received_amount = amount * exchange_rate
# #     received_amount -= received_amount * commission_rate
# #     return received_amount





# ''''''''''''''''''''




async def make_transaction(user, transaction_type, currency, payment_method, amount, commission=0):
    """
    Создает новую транзакцию.

    Args:
    - user: Пользователь, выполняющий транзакцию.
    - transaction_type: Тип транзакции ('send' или 'receive').
    - currency: Тип средства ('crypto', 'fiat' или 'money').
    - payment_method: Способ оплаты ('bank' или 'wallet').
    - amount: Сумма транзакции.
    - commission: Комиссия за транзакцию (по умолчанию 0).

    Returns:
    - Boolean: True, если транзакция успешно создана, False в противном случае.
    """
    try:
        transaction = Transaction.objects.create(
            user=user,
            transaction_type=transaction_type,
            currency=currency,
            payment_method=payment_method,
            amount=amount,
            commission=commission
        )
        return True
    except Exception as e:
        print(f"Error creating transaction: {e}")
        return False














