
from django.contrib import admin
from .models import Transaction  # Import your Transaction model

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'transaction_date', 'transaction_description', 'user', 'is_active', 'created_at', 'updated_at')  # Fields to display in the admin list view
    list_filter = ('transaction_date', 'user', 'is_active')  # Filters for the list view
    search_fields = ('transaction_description', 'user__username')  # Fields to search
