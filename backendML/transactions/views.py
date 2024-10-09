from django.http import JsonResponse
from .models import Transaction, FraudDetectionResult

# Create your views here.
# views for submitting the transaction data

def submit_transaction(request):
    if request.method == 'POST':
        transaction_id = request.POST.get('transaction_id')
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        phone_number = request.POST.get('phone_number')
        Receiver = request.POST.get('Receiver')
        security_key = request.POST.get('security_key')
        # save the transaction data
        transaction = Transaction.objects.create(
            transaction_id=transaction_id,
            amount=amount
        )
        return JsonResponse({"message": "Transaction submitted", "transaction_id": transaction.transaction_id})

def get_fraud_result(request, transaction_id):
    try:
        transaction = Transaction.objects.get(transaction_id=transaction_id)
        transaction_log = TransactionLog.objects.get(transaction=transaction)
        return JsonResponse({"result": transaction_log.result, "probability": transaction_log.probability})
    except Transaction.DoesNotExist:
        return JsonResponse({"error": "Transaction not found"}, status=404)
