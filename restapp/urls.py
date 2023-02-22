from django.urls import include, path
from rest_framework import routers
from restapp import views

#==========================================================================================
# Request router (browsable api's)   Example: http://127.0.0.1:8000/fds/browse/api/trains 
#==========================================================================================
router = routers.DefaultRouter()
router.register(r'api/users', views.UserViewSet)         
router.register(r'api/groups', views.GroupViewSet)       
router.register(r'api/trains', views.TrainViewSet)   
router.register(r'api/stations', views.StationViewSet)   
router.register(r'api/stops', views.StopViewSet) 
router.register(r'api/restaurants', views.RestaurantViewSet) 
router.register(r'api/menuitems', views.RestMenuViewSet) 
router.register(r'api/orders', views.OrderViewSet) 
router.register(r'api/items', views.OrderItemViewSet) 
router.register(r'api/payments', views.PaymentViewSet) 

# Any pattern use router
urlpatterns = [
    path('browse/', include(router.urls)),
    
    # to show login logout option
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))   
]


#=====================================================================================================================
# REST API's Endpoints                                               http://127.0.0.1:8000/fds/rest/api/...
#=====================================================================================================================

urlpatterns += [

    path('rest/api/users/', views.UserList.as_view()),               # http://127.0.0.1:8000/fds/rest/api/users/   **NOT WORKING
    path('rest/api/groups/', views.GroupList.as_view()),             # http://127.0.0.1:8000/fds/rest/api/groups/  **NOT WORKING
    
    path('rest/api/trains/', views.TrainList.as_view()),             # http://127.0.0.1:8000/fds/restapi/trains/    
    path('rest/api/stations/', views.StationList.as_view()),         # http://127.0.0.1:8000/fds/rest/api/stations/
    path('rest/api/stops/', views.StopList.as_view()),               # http://127.0.0.1:8000/fds/rest/api/stops/

    path('rest/api/restaurants/', views.RestaurantList.as_view()),   # http://127.0.0.1:8000/fds/rest/api/restaurants/
    path('rest/api/menuitems/', views.RestaurantList.as_view()),     # http://127.0.0.1:8000/fds/rest/api/menuitems/

    path('rest/api/orders/', views.OrderList.as_view()),             # http://127.0.0.1:8000/fds/rest/api/orders/ 
    path('rest/api/items/', views.OrderItemList.as_view()),          # http://127.0.0.1:8000/fds/rest/api/items/ 
    path('rest/api/payments/', views.PaymentList.as_view()),         # http://127.0.0.1:8000/fds/rest/api/payments/ 

 
    path('api/core/trains/<int:id>/', views.TrainDetail.as_view()),  # **NOT WORKING

]


