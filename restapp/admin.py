from django.contrib import admin
from .models import Train, Station, Stop, Restaurant, RestMenu, Order, OrderItem, Payment

# Controls the fields to display in admin panel
class TrainAdmin(admin.ModelAdmin):
    list_display = ('id', 'train_no', 'train_name')
    
class StationAdmin(admin.ModelAdmin):
    list_display = ('id', 'station_code', 'station_name')
    
class StopAdmin(admin.ModelAdmin):
    list_display = ('id', 'train_no', 'stop_no', 'station_code', 'arrival_time', 'departure_time', 'halt', 'day')    

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'rest_id', 'rest_name', 'rest_address', 'rest_location_code', 'user_id', 
                    'rest_type','rest_status', 'rest_rating')
    
class RestMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'menu_id', 'rest_id', 'item_name', 'item_desc', 'item_type',
                    'item_rate', 'item_discount', 'item_rating', 'item_status')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'rest_id', 'order_date', 'delivery_date', 'user_id',
                    'contact_no', 'station_code', 'train_no', 
                    'coach_no', 'seat_no', 'order_status', 'item_count', 'total_amount',
                    'total_discount', 'tax', 'net_amount')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_id', 'item_name', 'item_quantity' , 'item_rate' , 'item_discount' , 'order_id')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'payment_id' , 'order_id', 'payment_date' , 'payment_amount' , 
                    'payment_mode' , 'payment_ref','payment_status')
    

# Register the models
admin.site.register(Train, TrainAdmin)
admin.site.register(Station, StationAdmin)
admin.site.register(Stop, StopAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(RestMenu, RestMenuAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Payment, PaymentAdmin)

