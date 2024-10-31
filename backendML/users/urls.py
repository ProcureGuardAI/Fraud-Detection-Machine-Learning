# users/urls.py
from django.urls import path
from .views import RegisterAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register_user'),
    path('login/', LoginView.as_view())
]