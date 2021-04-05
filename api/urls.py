from django.urls import include, path
# The REST Framework router will make sure our requests end up at the right resource dynamically.
from rest_framework import routers
from . import views

# Register URL
# Using routers from Rest framework allow us to have some URLs solved for example:
# Query all users will be: /users (GET)
# Get one specific user will be: /users/<user_id> (GET)

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'orders', views.OrderViewSet)
router.register(r'shippings', views.ShippingViewSet)
router.register(r'payments', views.PaymentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

ordersByParam = views.OrderViewSet.as_view({
    'get': 'ordersByParam'
})

ordersByUser = views.OrderViewSet.as_view({
    'get': 'ordersByUser'
})

ordersByShipping = views.OrderViewSet.as_view({
    'get': 'ordersByShipping'
})

allUsers = views.UserViewSet.as_view({
    'get': 'allUsers',
    'post': 'createUser'
})

userId = views.UserViewSet.as_view({
    'get': 'userId'
})

urlpatterns = [
    path('', include(router.urls)),
    path('users/all/', allUsers, name='allUsers'),
    path('users/', allUsers, name='createUser'),
    path('users/<user_id>/', userId, name='userId'),
    path('orders/shipping/', ordersByShipping, name='ordersByShipping'),
    path('orders/<param>/', ordersByParam, name='ordersByParam'),
    path('orders/user/<user_id>/', ordersByUser, name='ordersByUser'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]