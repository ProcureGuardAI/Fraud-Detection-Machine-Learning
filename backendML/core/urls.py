# core/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet  # Import the view set for your concrete model

# Create a router and register your view sets
router = DefaultRouter()
router.register(r'transactions', TransactionViewSet, basename='transaction')  # Only register the Transaction view set

urlpatterns = [
    path('', include(router.urls)),  # Include the registered routes
]
