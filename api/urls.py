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

orders = views.OrderViewSet.as_view({
    'get': 'all_orders',
    'post': 'create_order'
})

order_by_param = views.OrderViewSet.as_view({
    'get': 'order_by_param'
})

orders_by_user = views.OrderViewSet.as_view({
    'get': 'orders_by_user'
})

orders_by_shipping = views.OrderViewSet.as_view({
    'get': 'orders_by_shipping'
})

all_user = views.UserViewSet.as_view({
    'get': 'all_user',
    'post': 'create_user'
})

user_id = views.UserViewSet.as_view({
    'get': 'user_id'
})

order_shipping_details = views.OrderViewSet.as_view({
    'get': 'order_shipping_details'
})

order_payment_details = views.OrderViewSet.as_view({
    'get': 'order_payment_details'
})

urlpatterns = [
    path('', include(router.urls)),
    path('users/', all_user, name='all_user'),
    path('users/', all_user, name='create_user'),
    path('users/<user_id>/', user_id, name='user_id'),
    path('order/<order_id>/shipping/detail/', order_shipping_details, name='order_shipping_details'),
    path('order/<order_id>/payment/detail/', order_payment_details, name='order_payment_details'),
    path('orders/shipping/', orders_by_shipping, name='orders_by_shipping'),
    path('orders/', orders, name='create_order'),
    path('orders/', orders, name='all_orders'),
    path('orders/<param>/', order_by_param, name='order_by_param'),
    path('orders/user/<user_id>/', orders_by_user, name='orders_by_user'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
