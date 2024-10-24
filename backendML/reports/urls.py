from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReportListView

router = DefaultRouter()
router.register(r'reports', ReportListView)

urlpatterns = [
    path('', include(router.urls)),
]