from django.db import models
from django.urls import reverse

# =======================================================================================================
# Note:
# -----
# (1) The inbuilt record id's from database are not used as primary keys (identifiers), we want more
#     control and meaning in the keys. Foreign key relationships have been commented for same reason.
#     Data integrity is ensure programatically.
# 
# (2) We are using our own AppUsers table in place of django's User table for similar reasons, have more
#     controls and meaningful identify assignment to the entities.
#
# =======================================================================================================

# App User
class AppUser(models.Model):    
    user_id = models.CharField(max_length = 15)                                          #Example: UID001
    user_name = models.CharField(max_length = 40,)                                     
    user_email = models.CharField(max_length = 40,)     
    user_mobile = models.CharField(max_length = 10,) 
    user_password = models.CharField(max_length = 40,)  
    ROLE_TYPE = (
            ('1','customer'),
            ('2','restaurant'),
        )                                                                    
    user_role = models.CharField(max_length = 1,choices=ROLE_TYPE,blank=False,default=1)     

    class Meta:
        ordering = ['user_id']

    def get_absolute_url(self):
        return reverse('user_id', args=[str(self.id)])   
        
    def __str__(self):
        return self.user_id
    
# Train Model
class Train(models.Model):    
    train_no = models.CharField(max_length = 8)                                         #Example: 12926
    train_name = models.CharField(max_length = 40,)                                     #Example: Paschim SF Express

    class Meta:
        ordering = ['train_no']

    def get_absolute_url(self):
        return reverse('train-detail', args=[str(self.id)])   
        
    def __str__(self):
        return self.train_no  


# Station Model
class Station(models.Model):    
    station_code = models.CharField(max_length = 8)                                     #Example: RTM  
    station_name = models.CharField(max_length = 40)                                    #Example: Ratlam

    class Meta:
        ordering = ['station_code']

    def get_absolute_url(self):
        return reverse('station-detail', args=[str(self.id)])   
        
    def __str__(self):
        return self.station_code  
    
# Stop Model
class Stop(models.Model): 
    train_no = models.CharField(max_length = 8)                                         #Example: 12926
    # train_no = models.ForeignKey('Train', on_delete=models.SET_NULL, null=True)       #Intentionally removed
    stop_no = models.CharField(max_length = 2)                                          #Example: 2
    station_code = models.CharField(max_length = 8)                                     #Example: RTM  
    # station_code = models.ForeignKey('Station', on_delete=models.SET_NULL, null=True) #Intentionally removed
    arrival_time = models.CharField(max_length = 5)                                     #Example: 07:20
    departure_time = models.CharField(max_length = 5)                                   #Example: 07:25
    halt = models.CharField(max_length = 4,)                                            #Example: 5m
    day = models.CharField(max_length = 5)                                              #Example: Day 1

    class Meta:
        ordering = ['train_no', 'stop_no']

    def get_absolute_url(self):
        return reverse('stop-detail', args=[str(self.id)])   
        
    def __str__(self):        
        return self.stop_no
    
# Restaurant Model
class Restaurant(models.Model):    
    rest_id = models.CharField(max_length = 15)                                         #Example: RID001
    rest_name = models.CharField(max_length = 40,help_text='Restaurant Name')           #Example: Haldiram
    rest_address = models.CharField(max_length = 120)                                   #Example: 34, Street A, City B - 123456
    rest_location_code = models.CharField(max_length = 8)                               #Example: RTM
    # rest_location_code = models.ForeignKey('Station', on_delete=models.SET_NULL, null=True)  #Intentionally removed
    rest_owner = models.CharField(max_length = 15,default="-")                          #Example: UID002
    contact_person = models.CharField(max_length = 40,default="-")                      #Example: Jatin Kumar
    contact_no = models.CharField(max_length = 10,default="-")                          #Example: 9812398123
    REST_TYPE = (
            ('0','Veg'),
            ('1','Non-Veg'),
        )                                            
    rest_type = models.CharField(max_length = 1,choices=REST_TYPE,blank=False,default='0')   
    rest_rating = models.IntegerField(default=0)                                        #Example: 4
    REST_STATUS = (
            ('1', 'Open'),
            ('0', 'Closed'),
        )
    rest_status = models.CharField(max_length = 1,choices=REST_STATUS, blank=False,default='1')  

    class Meta:
        ordering = ['rest_id']

    def get_absolute_url(self):
        return reverse('restaurant-detail', args=[str(self.id)])   
        
    def __str__(self):
        return self.rest_id

# Menu Model
class RestMenu(models.Model):    
    menu_id = models.CharField(max_length = 20)                                         #Example: MID3131464
    rest_id = models.CharField(max_length = 15)                                         #Example: RID001
    # rest_id = models.ForeignKey('Restaurant', on_delete=models.SET_NULL, null=True)   #Intentionally removed
    item_name = models.CharField(max_length = 40)                                       #Example: Veg Thali
    item_desc = models.CharField(max_length = 120)                                      #Example: 3 Chapati, Rice, Tadka Dal, Mix Veg, Salad, Sweets
    ITEM_TYPE = (
            ('0','Veg'),
            ('1','Non-Veg'),
        )
    item_type = models.CharField(max_length = 1,choices=ITEM_TYPE,blank=False,default='0') 
    item_rate = models.DecimalField(max_digits=6, decimal_places=2)                     #Example: 25.00
    item_discount = models.DecimalField(max_digits=6, decimal_places=2)                 #Example: -3:25
    item_rating = models.IntegerField(default=0)                                        #Example: 4
    MENU_ITEM_STATUS = (
            ('1', 'Available'),
            ('0', 'Unavailable'),
        )
    item_status = models.CharField(max_length = 1,choices=MENU_ITEM_STATUS, blank=False,default='1')
    
    class Meta:
        ordering = ['item_name']

    def get_absolute_url(self):
        return reverse('menu-detail', args=[str(self.id)])   
        
    def __str__(self):
        return self.menu_id 

# Order Model
class Order(models.Model):    
    order_id = models.CharField(max_length = 15)                                        #Example: OID2300001
    rest_id = models.CharField(max_length = 15)                                         #Example: RID001
    # rest_id = models.ForeignKey('Restaurant', on_delete=models.SET_NULL, null=True)   #Intenteionally removed
    order_date = models.DateField(null=True, blank=False)                               #Example: 2023-02-02
    delivery_date = models.DateField(null=True, blank=False)                            #Example: 2023-02-02
    user_id = models.CharField(max_length = 15)                                         #Example: UID001
    contact_no = models.CharField(max_length = 10)                                      #Example: 9812398123
    station_code = models.CharField(max_length = 8)                                     #Example: RTM  
    train_no = models.CharField(max_length = 8)                                         #Example: 12926
    # station_code = models.ForeignKey('Station', on_delete=models.SET_NULL, null=True) #Intenteionally removed
    # train_no = models.ForeignKey('Train', on_delete=models.SET_NULL, null=True)       #Intenteionally removed
    coach_no = models.CharField(max_length = 4)                                         #Example: B1
    seat_no = models.IntegerField(default=0)                                            #Example: 22
    ORDER_STATUS = (
            ('0' , 'Initial'),                   # When created, but payment pending   
            ('2' , 'Pending'),                   # When paid but not confirmed by restaurant
            ('3' , 'Confirmed'),                 # Confirmed by restaurant 
            ('4' , 'Rejected'),                  # Rejected by restaurant
            ('6' , 'Order Ready'),
            ('7' , 'In Transit'),
            ('8' , 'Delivered'),
            ('9' , 'Delivery Failed'),
            ('10', 'Cancelled'),
        )
    order_status = models.CharField(max_length = 2,choices=ORDER_STATUS,blank=False,default='0') 
    item_count = models.IntegerField(default=0)                                         #Example: 4
    total_amount = models.DecimalField(max_digits=6, decimal_places=2)                  #Example: 300:50
    total_discount = models.DecimalField(max_digits=6, decimal_places=2)                #Example: -40:00
    tax = models.DecimalField(max_digits=6, decimal_places=2)                           #Example:  20:00
    net_amount = models.DecimalField(max_digits=6, decimal_places=2)                    #Example: 280:50

    class Meta:
        ordering = ['order_id']

    def get_absolute_url(self):
        return reverse('order-detail', args=[str(self.id)])   
        
    def __str__(self):
        return self.order_id  

# Item Model
class OrderItem(models.Model):    
    item_id = models.CharField(max_length = 10)                                     #Example: OITM0001
    item_name = models.CharField(max_length = 40)                                   #Example: Thali
    item_quantity = models.IntegerField(default=0)                                  #Example: 2
    item_rate = models.DecimalField(max_digits=6, decimal_places=2)                 #Example: 25.00
    item_discount = models.DecimalField(max_digits=6, decimal_places=2)             #Example: -3:25
    order_id = models.CharField(max_length = 15)                                    #Example: OID2300001 (OIDYY99999)
    # order_id = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True)   #Intentionally removed  

    class Meta:
        ordering = ['item_id']

    def get_absolute_url(self):
        return reverse('item-detail', args=[str(self.id)])   
        
    def __str__(self):
        return self.item_id    

# Payment Model
class Payment(models.Model):    
    payment_id = models.CharField(max_length = 15)                                  #Example: PID23000001 (PIDYY0099999)
    order_id = models.CharField(max_length = 15)                                    #Example: OID2300001 (OIDYY99999)
    # order_id = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True)   #Intentionally removed
    payment_date = models.DateField(null=True, blank=False)                         #Example: YYYY-MM-DD
    payment_amount = models.DecimalField(max_digits=6, decimal_places=2)            #Example: 25.00
    payment_mode = models.CharField(max_length = 10)                                #Example: Card
    payment_ref = models.CharField(max_length = 20)                                 #Example: TRN20230220S0001
    PAYMENT_STATUS = (
            ('1', 'Success'),
            ('0', 'Failed'),
        )
    payment_status = models.CharField(max_length = 1,choices=PAYMENT_STATUS,blank=False, default='0')  

    class Meta:
        ordering = ['payment_id']

    def get_absolute_url(self):
        return reverse('item-detail', args=[str(self.id)])   
        
    def __str__(self):
        return self.payment_id   
