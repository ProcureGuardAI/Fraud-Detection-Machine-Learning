from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from core import views as core_views


# Import views 

router = routers.DefaultRouter()

# urlpatterns = router.urls
router.register(r'transactions', core_views.TransactionViewSet, basename='transaction')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Include the router URLs (if using viewsets)
    
    # API endpoints for each app
    path('api/users/', include('users.urls')),
    path('api/notifications/', include('notifications.urls')),
    path('api/reports/', include('reports.urls')),
    path('api/core', include('core.urls'))

]