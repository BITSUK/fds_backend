
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

class FilteredStopList(generics.ListAPIView):
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
        
# Restaurant
class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class FilteredRestaurantList(generics.ListAPIView):
    serializer_class = RestaurantSerializer
    def get_queryset(self):
        queryset = Restaurant.objects.all()
        station = self.request.query_params.get('station_code', None)
        type = self.request.query_params.get('rest_type', None)
        rating = self.request.query_params.get('rest_rating', None)
        status = self.request.query_params.get('rest_status', None)
        if (station is not None):
            queryset = queryset.filter(rest_location_code = station)
        if (type is not None):
            queryset = queryset.filter(rest_type = type)
        if (rating is not None):
            queryset = queryset.filter(rest_rating = rating)
        if (status is not None):
            queryset = queryset.filter(rest_status = status)
        return queryset

# Restaurant Menu
class RestMenuList(generics.ListCreateAPIView):
    queryset = RestMenu.objects.all()
    serializer_class = RestMenuSerializer

class RestMenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RestMenu.objects.all()
    serializer_class = RestMenuSerializer

class FilteredMenuItemList(generics.ListAPIView):
    serializer_class = RestMenuSerializer
    def get_queryset(self):
        queryset = RestMenu.objects.all()
        rest = self.request.query_params.get('rest_id', None)
        if (rest is not None):
            queryset = queryset.filter(rest_id = rest)
        return queryset

# Order
class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class FilteredOrderList(generics.ListAPIView):
    serializer_class = OrderSerializer
    def get_queryset(self):
        queryset = Order.objects.all()
        user = self.request.query_params.get('user_id', None)
        rest = self.request.query_params.get('rest_id', None)
        station = self.request.query_params.get('station_code', None)
        status = self.request.query_params.get('order_status', None)
        if (user is not None):
            queryset = queryset.filter(user_id = user)
        if (rest is not None):
            queryset = queryset.filter(rest_id = rest)
        if (station is not None):
            queryset = queryset.filter(station_code = station)
        if (status is not None):
            queryset = queryset.filter(order_status = status)
        return queryset
    
# Order Item
class OrderItemList(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class FilteredOrderItemList(generics.ListAPIView):
    serializer_class = OrderItemSerializer
    def get_queryset(self):
        queryset = OrderItem.objects.all()
        order = self.request.query_params.get('order_id', None)
        if (order is not None):
            queryset = queryset.filter(order_id = order)
        return queryset
    
# Payment
class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class FilteredPaymentList(generics.ListAPIView):
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