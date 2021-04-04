from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import UserSerializer, OrderSerializer, ShippingSerializer, PaymentSerializer
from .models import Users, Orders, Shippings, Payments

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('name')
    serializer_class = UserSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

class ShippingViewSet(viewsets.ModelViewSet):
    queryset = Shippings.objects.all()
    serializer_class = ShippingSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentSerializer