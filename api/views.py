from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, OrderSerializer, ShippingSerializer, PaymentSerializer
from .models import Users, Orders, Shippings, Payments


class UserViewSet(viewsets.ViewSet):
    """ View User """
    permission_classes = (IsAuthenticated,)

    def allUsers(self, request):
        """ Method that return all users"""
        queryset = Users.objects.all().order_by('name')
        serializer = UserSerializer(queryset, many=True)

        return Response(serializer.data)

    def userId(self, request, user_id):
        """ Method that return user by id"""
        queryset = Users.objects.filter(user_id=user_id)
        serializer = UserSerializer(queryset, many=True)

        return Response(serializer.data)

    def createUser(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderViewSet(viewsets.ViewSet):
    """ View Order """
    permission_classes = (IsAuthenticated,)

    def allOrders(self, request):
        """ Method that return all orders"""
        queryset = Orders.objects.all()
        serializer = OrderSerializer(queryset, many=True)

        return Response(serializer.data)

    def ordersByParam(self, request, param):
        """ Method that return order by Id or Ids or dates """
    
        if param.find("-") != -1:
            date_start = param[0:10]
            date_end = param[11:21]

            queryset = Orders.objects.filter(date__range=(date_start, date_end))
            serializer = OrderSerializer(queryset, many=True)
        else:
            ids = param.split(",")
            queryset = Orders.objects.filter(order_id__in=ids)
            serializer = OrderSerializer(queryset, many=True)

        return Response(serializer.data)
    
    def ordersByUser(self, request, user_id):
        """ Method that return order by user id """
        queryset = Orders.objects.filter(user__user_id=user_id)
        serializer = OrderSerializer(queryset, many=True)
        
        return Response(serializer.data)

    def ordersByShipping(self, request):
        """ Method that return order by user id """
        queryDict = request.query_params
        ordersIds = Shippings.objects.filter(city__exact=queryDict.get('city')).filter(state__exact=queryDict.get('state')).filter(country__exact=queryDict.get('country')).values_list('order')
        orders = Orders.objects.filter(order_id__in=ordersIds)
        serializer = OrderSerializer(orders, many=True)

        return Response(serializer.data)
    
    def orderShippingDetails(self, request, order_id):
        """ """
        shipping = Shippings.objects.get(order_id=order_id)
        serializer = ShippingSerializer(shipping)
        
        return Response(serializer.data)

    def orderPaymentDetails(self, request, order_id):
        """ """
        payments = Payments.objects.filter(order_id__exact=order_id)
        serializer = PaymentSerializer(payments, many=True)
        
        return Response(serializer.data)
    
    def createOrder(self, request):
        serializer = OrdersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShippingViewSet(viewsets.ModelViewSet):
    """ View Shipping """
    permission_classes = (IsAuthenticated,)

    queryset = Shippings.objects.all()
    serializer_class = ShippingSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    """ View Payment """
    permission_classes = (IsAuthenticated,)
    queryset = Payments.objects.all()
    serializer_class = PaymentSerializer