from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from core import views as core_views
from rest_framework.authtoken.views import obtain_auth_token

# Import views 

router = routers.DefaultRouter()

# urlpatterns = router.urls
router.register(r'transactions', core_views.TransactionViewSet, basename='transaction')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Include the router URLs (if using viewsets)
    
    path('api/users/', include('users.urls')),
    path('api/notifications/', include('notifications.urls')),
    path('api/reports/', include('reports.urls')),
    path('api/core', include('core.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Add this line

]