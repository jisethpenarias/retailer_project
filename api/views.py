from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer, OrderSerializer, ShippingSerializer, PaymentSerializer
from .models import Users, Orders, Shippings, Payments

class UserViewSet(viewsets.ViewSet):
    """ View User """

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

    def orders(self, request):
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
        queryset = Orders.objects.filter(shipping__city=(queryDict.get('city'))).filter(shipping__state=(queryDict.get('state'))).filter(shipping__country=(queryDict.get('country')))
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

class ShippingViewSet(viewsets.ModelViewSet):
    """ View Shipping """
    queryset = Shippings.objects.all()
    serializer_class = ShippingSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    """ View Payment """
    queryset = Payments.objects.all()
    serializer_class = PaymentSerializer