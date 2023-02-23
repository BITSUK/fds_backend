
from django.contrib.auth.models import User, Group
from restapp.models import AppUser, Train, Station, Stop, Restaurant, RestMenu, Order, OrderItem, Payment

from restapp.serializers import AppUserSerializer, SysUserSerializer, SysGroupSerializer
from restapp.serializers import TrainSerializer, StationSerializer, StopSerializer
from restapp.serializers import RestaurantSerializer, RestMenuSerializer
from restapp.serializers import OrderSerializer, OrderItemSerializer, PaymentSerializer

#===================================================================
# Using Generics 
#===================================================================

from rest_framework import generics

# App User 
class AppUserList(generics.ListCreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

class AppUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

#Train                                               
class TrainList(generics.ListCreateAPIView):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer

class TrainDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer

# Stations
class StationList(generics.ListCreateAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

class StationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

# Stop
class StopList(generics.ListCreateAPIView):
    queryset = Stop.objects.all()
    serializer_class = StopSerializer

class StopDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stop.objects.all()
    serializer_class = StopSerializer

# Restaurant
class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

# Restaurant Menu
class RestMenuList(generics.ListCreateAPIView):
    queryset = RestMenu.objects.all()
    serializer_class = RestMenuSerializer

class RestMenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RestMenu.objects.all()
    serializer_class = RestMenuSerializer

# Order
class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# Order Item
class OrderItemList(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

# Payment
class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

# Sys User 
class SysUserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = SysUserSerializer

class SysUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = SysUserSerializer

# Sys Group
class SysGroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = SysGroupSerializer

class SysGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = SysGroupSerializer