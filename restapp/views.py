from rest_framework import viewsets
from rest_framework import permissions

from django.contrib.auth.models import User, Group
from restapp.models import Train, Station, Stop, Restaurant, RestMenu, Order, OrderItem, Payment

from restapp.serializers import UserSerializer, GroupSerializer
from restapp.serializers import TrainSerializer, StationSerializer, StopSerializer
from restapp.serializers import RestaurantSerializer, RestMenuSerializer
from restapp.serializers import OrderSerializer, OrderItemSerializer, PaymentSerializer



# Users 
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

# User Groups
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

# Train 
class TrainViewSet(viewsets.ModelViewSet):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer
    permission_classes = [permissions.IsAuthenticated]   

# Stations
class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = [permissions.IsAuthenticated]    

# Stop
class StopViewSet(viewsets.ModelViewSet):
    queryset = Stop.objects.all()
    serializer_class = StopSerializer
    permission_classes = [permissions.IsAuthenticated]        

# Restaurant
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated]      

# Restaurant Menu
class RestMenuViewSet(viewsets.ModelViewSet):
    queryset = RestMenu.objects.all()
    serializer_class = RestMenuSerializer
    permission_classes = [permissions.IsAuthenticated]      

# Order
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]      

# Order Item
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]    

# Payment
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]  