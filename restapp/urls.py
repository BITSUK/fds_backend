from django.urls import include, path
from rest_framework import routers
from restapp import views
from restapp import views_authentication
from restapp import views_custom

#============================================================================
# API URLs        
# -------             
# They start with http://127.0.0.1:8000/fds/rest/api/...
#============================================================================
urlpatterns = [                                 

    # =============
    # Users
    # =============
    path('rest/api/users/', views.AppUserList.as_view()),                                  
    path('rest/api/users/<int:pk>', views.AppUserDetail.as_view()),  
    path('rest/api/users/registration/', views_authentication.RegisterUserAPI),            # Custom endpoint
    path('rest/api/users/login/', views_authentication.LoginAPI),                          # Custom endpoint
    path('rest/api/users/change_password/', views_authentication.ChangePasswordAPI),       # Custom endpoint

    # =============
    # Trains
    # =============
    path('rest/api/trains/', views.TrainList.as_view()),             
    path('rest/api/trains/<int:pk>', views.TrainDetail.as_view()),  

    # =============
    # Stations
    # =============
    path('rest/api/stations/', views.StationList.as_view()),         
    path('rest/api/stations/<int:pk>', views.StationDetail.as_view()),  

    # =============
    # Stops
    # =============
    path('rest/api/stops/', views.StopList.as_view()),               
    path('rest/api/stops/<int:pk>', views.StopDetail.as_view()),  

    # =============
    # Restaurants
    # =============
    path('rest/api/restaurants/', views.RestaurantList.as_view()),   
    path('rest/api/restaurants/<int:pk>', views.RestaurantDetail.as_view()), 
    path('rest/api/restaurants/registration/', views_custom.RegisterRestAPI),          # Custom endpoint 
    
    # =============
    # Menu Items
    # =============
    path('rest/api/menuitems/', views.RestMenuList.as_view()),       
    path('rest/api/menuitems/<int:pk>', views.RestMenuDetail.as_view()),  

    # =============
    # Orders
    # =============
    path('rest/api/orders/', views.OrderList.as_view()),                           
    path('rest/api/orders/<int:pk>', views.OrderDetail.as_view()),  
    path('rest/api/orders/create_order/', views_custom.CreateOrder),                   # Custom endpoints

    # =============
    # Order Items
    # =============
    path('rest/api/items/', views.OrderItemList.as_view()),          
    path('rest/api/items/<int:pk>', views.OrderItemDetail.as_view()),  

    # =============
    # Payments
    # =============
    path('rest/api/payments/', views.PaymentList.as_view()),         
    path('rest/api/payments/<int:pk>', views.PaymentDetail.as_view()),  

    # =============
    # Users                                                 // Not used currently, exposed for learning purpose
    # =============
    path('rest/api/sysusers/', views.SysUserList.as_view()),               
    path('rest/api/sysusers/<int:pk>', views.SysUserDetail.as_view()),  

    # =============
    # Groups                                               // Not used currently, exposed for learning purpose  
    # =============
    path('rest/api/sysgroups/', views.SysGroupList.as_view()),             
    path('rest/api/sysgroups/<int:pk>', views.SysGroupDetail.as_view()), 

]


