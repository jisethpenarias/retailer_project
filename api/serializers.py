from rest_framework import serializers
from .models import Users, Orders, Shippings, Payments

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('user_id', 'name', 'last_name', 'gov_id', 'email', 'company')

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.name')
    shipping = serializers.ReadOnlyField(source='shipping.address')

    # user = serializers.HyperlinkedIdentityField(view_name='users', format='html')
    # shipping = serializers.HyperlinkedIdentityField(view_name='shippings', format='html')
 
    class Meta:
        model = Orders
        fields = ('order_id', 'user', 'shipping', 'date', 'total', 'subtotal', 'taxes', 'paid')

class ShippingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shippings
        fields = ('shipping_id', 'address', 'city', 'state', 'country', 'cost')

class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    order = serializers.ReadOnlyField(source='order.order_id')

    class Meta:
        model = Payments
        fields = ('payment_id', 'order', 'type', 'date', 'txn_id', 'total', 'status')
