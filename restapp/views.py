
from django.contrib.auth.models import User, Group
from restapp.models import AppUser, Train, Station, Stop, Restaurant, RestMenu, Order, OrderItem, Payment
from rest_framework.generics import GenericAPIView
from restapp.serializers import AppUserSerializer, SysUserSerializer, SysGroupSerializer
from restapp.serializers import TrainSerializer, StationSerializer, StopSerializer
from restapp.serializers import RestaurantSerializer, RestMenuSerializer
from restapp.serializers import OrderSerializer, OrderItemSerializer, PaymentSerializer

#===================================================================
# Using Generics 
#===================================================================

from rest_framework import generics

class API(GenericAPIView):
    serializer_class = AppUserSerializer

# User (App User)
class AppUserList(generics.ListCreateAPIView):
    serializer_class = AppUserSerializer
    def get_queryset(self):
        queryset = AppUser.objects.all()
        user = self.request.query_params.get('user_id', None)
        if (user is not None):
            queryset = queryset.filter(user_id = user)
        return queryset

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
    serializer_class = StopSerializer
    def get_queryset(self):
        queryset = Stop.objects.all()
        train = self.request.query_params.get('train_no', None)
        station = self.request.query_params.get('station_code', None)
        if (train is not None):
            queryset = queryset.filter(train_no = train)
        if (station is not None):
            queryset = queryset.filter(station_code = station)
        return queryset

class StopDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StopSerializer
    queryset = Stop.objects.all()
       
# Restaurant
class RestaurantList(generics.ListCreateAPIView):
    serializer_class = RestaurantSerializer
    def get_queryset(self):
        queryset = Restaurant.objects.all()
        station = self.request.query_params.get('station_code', None)
        type = self.request.query_params.get('rest_type', None)
        rating = self.request.query_params.get('rest_rating', None)
        status = self.request.query_params.get('rest_status', None)
        owner = self.request.query_params.get('rest_owner', None)
        rest = self.request.query_params.get('rest_id', None)
        if (station is not None):
            queryset = queryset.filter(rest_location_code = station)
        if (type is not None):
            queryset = queryset.filter(rest_type = type)
        if (rating is not None):
            queryset = queryset.filter(rest_rating = rating)
        if (status is not None):
            queryset = queryset.filter(rest_status = status)
        if (owner is not None):
            queryset = queryset.filter(rest_owner = status)
        if (rest is not None):
            queryset = queryset.filter(rest_id = rest)
        return queryset

class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

# Restaurant Menu
class RestMenuList(generics.ListCreateAPIView):
    serializer_class = RestMenuSerializer
    def get_queryset(self):
        queryset = RestMenu.objects.all()
        rest = self.request.query_params.get('rest_id', None)
        menu = self.request.query_params.get('menu_id', None)
        if (rest is not None):
            queryset = queryset.filter(rest_id = rest)
        if (menu is not None):
            queryset = queryset.filter(menu_id = menu)
        return queryset

class RestMenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RestMenu.objects.all()
    serializer_class = RestMenuSerializer

# Order
class OrderList(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    def get_queryset(self):
        queryset = Order.objects.all()
        user = self.request.query_params.get('user_id', None)
        rest = self.request.query_params.get('rest_id', None)
        station = self.request.query_params.get('station_code', None)
        status = self.request.query_params.get('order_status', None)
        order = self.request.query_params.get('order_id', None)
        if (user is not None):
            queryset = queryset.filter(user_id = user)
        if (rest is not None):
            queryset = queryset.filter(rest_id = rest)
        if (station is not None):
            queryset = queryset.filter(station_code = station)
        if (status is not None):
            queryset = queryset.filter(order_status = status)
        if (order is not None):
            queryset = queryset.filter(order_id = order)
        return queryset

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
 
# Order Item
class OrderItemList(generics.ListCreateAPIView):
    serializer_class = OrderItemSerializer
    def get_queryset(self):
        queryset = OrderItem.objects.all()
        order = self.request.query_params.get('order_id', None)
        if (order is not None):
            queryset = queryset.filter(order_id = order)
        return queryset

class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    
# Payment
class PaymentList(generics.ListCreateAPIView):
    serializer_class = PaymentSerializer
    def get_queryset(self):
        queryset = Payment.objects.all()
        order = self.request.query_params.get('order_id', None)
        status = self.request.query_params.get('order_status', None)
        if (order is not None):
            queryset = queryset.filter(order_id = order)
        if (status is not None):
            queryset = queryset.filter(order_status = status)
        return queryset

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