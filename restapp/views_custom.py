from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

import json

from restapp.models import Order, OrderItem, Restaurant, AppUser, Station
from restapp.serializers import OrderSerializer, OrderItemSerializer, RestaurantSerializer, AppUserSerializer

#============================================================================================
# Restaurant registration using custom endpoint
#============================================================================================
@api_view(['POST'])
def RegisterRestAPI(request):
	if request.method == 'POST':
		new_rest_data = JSONParser().parse(request)
		
		r_id = new_rest_data['rest_id']
		r_owner = new_rest_data['rest_owner']
		r_location_code = new_rest_data['rest_location_code']

		if r_id is not None and r_location_code is not None and r_owner is not None:	

			# Check if rest_owner is a user
			users = AppUser.objects.all()
			users = users.filter(user_id = r_owner) 		
			if (len(users) > 0):
				return JsonResponse({'message': 'Owner already has a restaurant registered.'}, status=status.HTTP_204_NO_CONTENT)
			
			# Check if rest_id already exists
			rests = Restaurant.objects.all()
			rests = rests.filter(rest_id = r_id) 		
			if (len(rests) > 0):
				return JsonResponse({'message': 'Restaurant id already exists.'}, status=status.HTTP_204_NO_CONTENT)

			# Check if rest_location_code is valid station_code
			stations = Station.objects.all()
			stations = stations.filter(station_code = r_location_code) 		
			if (len(stations) == 0):
				return JsonResponse({'message': 'Location code not recognised.'}, status=status.HTTP_204_NO_CONTENT)
			
			serializer = RestaurantSerializer(data=new_rest_data)	
			if serializer.is_valid():
				serializer.save()
				return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 
			else:
				return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		else:
				return JsonResponse({'message': 'Mandatory details missing.'}, status=status.HTTP_204_NO_CONTENT)  

#============================================================================================
# Order creation using custom endpoint
#============================================================================================
@api_view(['POST'])
def CreateOrder(request):
	if request.method == 'POST':
		return JsonResponse({'message': 'This request is under contruction.'}, status=status.HTTP_204_NO_CONTENT)  
		
		new_order_request = JSONParser().parse(request)
	
		new_order_data = 1 #extract order details from new_order_request
		new_order_items_data = 1 #extract order items details from new_order_request
		
		# Create Order
		serializer_order = OrderSerializer(data=new_order_data)
		
		if serializer_order.is_valid():
			serializer_order.save()

			# Create Order Items
			# <<Add a Loop>>
			serializer_orderitem = OrderItemSerializer(data=new_order_items_data)
			
			if serializer_orderitem.is_valid():
				serializer_orderitem.save()

				return JsonResponse(serializer_orderitem.data, status=status.HTTP_201_CREATED) 
			
			# Bad Request
			return JsonResponse(serializer_orderitem.errors, status=status.HTTP_400_BAD_REQUEST)	
			
		# Bad Request
		return JsonResponse(serializer_order.errors, status=status.HTTP_400_BAD_REQUEST)
		
		

