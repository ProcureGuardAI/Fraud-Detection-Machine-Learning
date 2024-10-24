from django.urls import path
from .views import RegisterAPIView
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'users', RegisterAPIView, basename='register')

urlpatterns = [
    path('register/', include(router.urls)),

]
