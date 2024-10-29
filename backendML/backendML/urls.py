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
    # creating the APIs
    path('training/', views.TrainChurnModel.as_view(), name = 'model_training'),
    path('prediction/', views.PredChurnModel.as_view(), name = 'model_prediction')

    path('api/users/', include('users.urls')),
    path('api/notifications/', include('notifications.urls')),
    path('api/reports/', include('reports.urls')),
    path('api/core', include('core.urls')),

    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Add this line

]