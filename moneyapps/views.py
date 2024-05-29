from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.exceptions import PermissionDenied
from .services import make_transaction
from .services import *
from .models import Transaction
from .serializers import TransactionSerializer
from drf_yasg.utils import swagger_auto_schema











@swagger_auto_schema(method='post', request_body=TransactionSerializer, responses={201: 'Created', 400: 'Bad Request'})
@api_view(['POST'])
def create_transaction(request):
    """
    Create a new transaction.
    """
    serializer = TransactionSerializer(data=request.data)
    if serializer.is_valid():
        # user = request.user
        transaction_type = serializer.validated_data['transaction_type']
        currency = serializer.validated_data['currency']
        payment_method = serializer.validated_data['payment_method']
        amount = serializer.validated_data['amount']
        commission = serializer.validated_data.get('commission', 0)

        success = make_transaction(user, transaction_type, currency, payment_method, amount, commission)
        if success:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response("Failed to create transaction.", status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





















kripta = get_crypto_rate('ids','vs_currencies')

fiatnie = get_fiat_rate('app_id','base')

# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from .models import Transaction
# from .serializers import TransactionSerializer

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def list_transactions_for_current_user(request):
#     try:
#         # Получаем транзакции только для текущего пользователя
#         transactions = Transaction.objects.filter(user=request.user)
#         # Сериализуем транзакции
#         serializer = TransactionSerializer(transactions, many=True)
#         # Возвращаем список транзакций в ответе
#         return Response(serializer.data)
#     except Exception as e:
#         # Если возникает ошибка, возвращаем сообщение об ошибке
#         return Response({"error": str(e)}, status=500)





















# @api_view(['GET'])
# def list_transactions(request):
#     transactions = Transaction.objects.filter(user=request.user)
#     serializer = TransactionSerializer(transactions, many=True)
#     return Response(serializer.data)




# @api_view(['GET'])
# def list_transactions(request):
#     if request.user.is_authenticated:
#         try:
#             transactions = Transaction.objects.filter(user=request.user)
#             # Ваш код для обработки транзакций
#         except Exception as e:
#             print('Ohibka')
#     else:
#         raise PermissionDenied()  # или выполните другие действия, соответствующие вашим требованиям




# from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse

# @login_required
# def list_transactions(request):
#     try:
#         # Проверяем, что запрос приходит от аутентифицированного пользователя
#         if request.user.is_authenticated:
#             # Получаем транзакции только для текущего пользователя
#             transactions = Transaction.objects.filter(user=request.user)
#             # Далее обрабатываем транзакции и возвращаем JsonResponse с результатом
#             # Ваш код для обработки транзакций
#             return JsonResponse({"transactions": transactions})
#         else:
#             # Если пользователь не аутентифицирован, возвращаем ошибку
#             return JsonResponse({"error": "Unauthorized"}, status=401)
#     except Exception as e:
#         # Обрабатываем возможные ошибки и возвращаем JsonResponse с сообщением об ошибке
#         return JsonResponse({"error": str(e)}, status=500)
