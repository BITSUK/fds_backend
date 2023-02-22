from rest_framework import serializers

from django.contrib.auth.models import User, Group
from restapp.models import Train, Station, Stop, Restaurant, RestMenu, Order, OrderItem, Payment

#==================================================================
# Using Hyper Linked Model Searializer 
#==================================================================

# User
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id' ,'url', 'username', 'email', 'groups']

# Group
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['id' ,'url', 'name']

# Train
class TrainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Train
        fields = ['id' , 'train_no', 'train_name']        

# Station
class StationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Station
        fields = ['id' ,'station_code', 'station_name']        

# Stop
class StopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stop
        fields = ['id' ,'train_no', 'stop_no', 'station_code', 'arrival_time', 'departure_time', 'halt', 'day']    

# Restaurant
class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id' ,'rest_id', 'rest_name', 'rest_address', 'rest_location_code', 'user_id', 
                    'rest_type','rest_status', 'rest_rating']   

# Restaurant Menu
class RestMenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RestMenu
        fields = ['id' ,'menu_id', 'rest_id', 'item_name', 'item_desc', 'item_type',
                    'item_rate', 'item_discount', 'item_rating', 'item_status']  

# Order
class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['id' ,'order_id', 'rest_id', 'order_date', 'delivery_date', 'user_id',
                    'contact_no', 'station_code', 'train_no', 
                    'coach_no', 'seat_no', 'order_status', 'item_count', 'total_amount',
                    'total_discount', 'tax', 'net_amount']  

# Order Item
class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id' ,'item_id', 'item_name', 'item_quantity' , 'item_rate' , 'item_discount' , 'order_id']  

# Payment
class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = ['id' ,'payment_id' , 'order_id', 'payment_date' , 'payment_amount' , 
                    'payment_mode' , 'payment_ref','payment_status']  
        
#==================================================================
# Using Model Searializer 
#==================================================================

# User
class UserSerializer2(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id' ,'url', 'username', 'email', 'groups']

# Group
class GroupSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id' ,'url', 'name']

# Train
class TrainSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = ['id' , 'train_no', 'train_name']        

# Station
class StationSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['id' ,'station_code', 'station_name']        

# Stop
class StopSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Stop
        fields = ['id' ,'train_no', 'stop_no', 'station_code', 'arrival_time', 'departure_time', 'halt', 'day']    

# Restaurant
class RestaurantSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id' ,'rest_id', 'rest_name', 'rest_address', 'rest_location_code', 'user_id', 
                    'rest_type','rest_status', 'rest_rating']   

# Restaurant Menu
class RestMenuSerializer2(serializers.ModelSerializer):
    class Meta:
        model = RestMenu
        fields = ['id' ,'menu_id', 'rest_id', 'item_name', 'item_desc', 'item_type',
                    'item_rate', 'item_discount', 'item_rating', 'item_status']  

# Order
class OrderSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id' ,'order_id', 'rest_id', 'order_date', 'delivery_date', 'user_id',
                    'contact_no', 'station_code', 'train_no', 
                    'coach_no', 'seat_no', 'order_status', 'item_count', 'total_amount',
                    'total_discount', 'tax', 'net_amount']  

# Order Item
class OrderItemSerializer2(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id' ,'item_id', 'item_name', 'item_quantity' , 'item_rate' , 'item_discount' , 'order_id']  

# Payment
class PaymentSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id' ,'payment_id' , 'order_id', 'payment_date' , 'payment_amount' , 
                    'payment_mode' , 'payment_ref','payment_status']  