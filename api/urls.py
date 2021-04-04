from django.urls import include, path
# The REST Framework router will make sure our requests end up at the right resource dynamically.
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'shippings', views.ShippingViewSet)
router.register(r'payments', views.PaymentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]