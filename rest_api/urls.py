from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'pens', views.PenViewSet)
router.register(r'snails-inventory', views.SnailsCurrentInventoryViewSet)
router.register(r'snails-activity', views.SnailsActivityViewSet)
router.register(r'eggs-inventory', views.EggsInventoryViewSet)
router.register(r'stock-transfers', views.StocksTransferViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
