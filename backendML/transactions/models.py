from django.db import models

# Create your models here.

class Transaction(models.Model):
    transaction_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=15)
    Receiver = models.DecimalField(max_digits=13, decimal_places=2)
    security_key = models.CharField(max_length=100) # this is after sending an OTP to the phone number

    def __str__(self):
        return f'{self.transaction_id} - {self.amount}'
    
class TransactionLog(models.Model):
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE)
    result = models.CharField(max_length=10)  # Could be Fraud or Legitimate
    probability = models.FloatField()

