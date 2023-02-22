from django.urls import include, path
from rest_framework import routers
from restapp import views

# Request router (browsable api's)
router = routers.DefaultRouter()
router.register(r'browse/api/users', views.UserViewSet)         
router.register(r'browse/api/groups', views.GroupViewSet)       
router.register(r'browse/api/trains', views.TrainViewSet)   
router.register(r'browse/api/stations', views.StationViewSet)   
router.register(r'browse/api/stops', views.StopViewSet) 
router.register(r'browse/api/restaurants', views.RestaurantViewSet) 
router.register(r'browse/api/orders', views.OrderViewSet) 
router.register(r'browse/api/items', views.OrderItemViewSet) 
router.register(r'browse/api/payments', views.PaymentViewSet) 


# Any pattern use router
urlpatterns = [
    path('', include(router.urls)),
    
    # to show login logout option
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))   
]
