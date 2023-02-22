from rest_framework import serializers

from django.contrib.auth.models import User, Group
from restapp.models import Train, Station, Stop, Restaurant, RestMenu, Order, OrderItem, Payment

#==================================================================
#Using Model Searializer approach
#==================================================================

# User
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

# Group
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

# Train
class TrainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Train
        fields = ['train_no', 'train_name']        

# Station
class StationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Station
        fields = ['station_code', 'station_name']        

# Stop
class StopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stop
        fields = ['train_no', 'stop_no', 'station_code', 'arrival_time', 'departure_time', 'halt', 'day']    

# Restaurant
class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['rest_id', 'rest_name', 'rest_address', 'rest_location_code', 'user_id', 
                    'rest_type','rest_status', 'rest_rating']   

# Restaurant Menu
class RestMenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RestMenu
        fields = ['menu_id', 'rest_id', 'item_name', 'item_desc', 'item_type',
                    'item_rate', 'item_discount', 'item_rating', 'item_status']  

# Order
class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['order_id', 'rest_id', 'order_date', 'delivery_date', 'user_id',
                    'contact_no', 'station_code', 'train_no', 
                    'coach_no', 'seat_no', 'order_status', 'item_count', 'total_amount',
                    'total_discount', 'tax', 'net_amount']  

# Order Item
class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['item_id', 'item_name', 'item_quantity' , 'item_rate' , 'item_discount' , 'order_id']  

# Payment
class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = ['payment_id' , 'order_id', 'payment_date' , 'payment_amount' , 
                    'payment_mode' , 'payment_ref','payment_status']  