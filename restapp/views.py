from rest_framework import viewsets
from rest_framework import permissions


from django.contrib.auth.models import User, Group
from restapp.models import Train, Station, Stop, Restaurant, RestMenu, Order, OrderItem, Payment

from restapp.serializers import UserSerializer, GroupSerializer
from restapp.serializers import TrainSerializer, StationSerializer, StopSerializer
from restapp.serializers import TrainModelSerializer
from restapp.serializers import RestaurantSerializer, RestMenuSerializer
from restapp.serializers import OrderSerializer, OrderItemSerializer, PaymentSerializer

#===================================================================
# Using Model View Set
#===================================================================
# Users 
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

# Groups
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


#===================================================================
# Using Generics API Views
# GET POST          --> generics.ListCreateAPIView  
# GET/pk PUT DELETE --> generics.RetrieveUpdateDestroyAPIView
#===================================================================

from rest_framework import generics

# User
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Group
class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

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
