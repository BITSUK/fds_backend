from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

import json

from restapp.models import AppUser, Restaurant
from restapp.serializers import AppUserSerializer, RestaurantSerializer

#============================================================================================
# User registration using custom endpoint
#============================================================================================
@api_view(['POST'])
def RegisterUserAPI(request):
	if request.method == 'POST':
		new_user_data = JSONParser().parse(request)
		
		user_id = new_user_data['user_id']
		user_name = new_user_data['user_name']
		user_email = new_user_data['user_email']
		user_password = new_user_data['user_password']	
		user_role = new_user_data['user_role']	
		rest_id = new_user_data['rest_id']

		if user_id is not None and user_name is not None and user_role is not None and user_password is not None:	
			users = AppUser.objects.all()
			users = users.filter(user_id__icontains = user_id) 		
			rests = Restaurant.objects.all()
			rests = rests.filter(rest_id__icontains = rest_id) 

			# last_uid = users.reverse()[0].user_id
			# next_uid = last_uid[0:3] + str(int(last_uid[3:]) + 1)
			# user_id = next_uid

			if (len(users) == 0) :	                                # Check if record already exists
				if (user_role == "1" or user_role == "2"):			# Validate role
					serializer = AppUserSerializer(data=new_user_data)					
					if serializer.is_valid():

						if ((user_role == "2") and (len(rests) == 0)):                  # check for creating restaurant record
							rest_serializer = RestaurantSerializer(data=new_user_data)	
							if rest_serializer.is_valid():
								serializer.save()                                       # User created
								rest_serializer.save()                                  # Restaurant created
								return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 
							else:
								return JsonResponse({'message': 'Registration Failed.'}, status=status.HTTP_400_BAD_REQUEST) 
						else:
							serializer.save()                                           # User created 
							return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 
					else:
						return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
				else:
					return JsonResponse({'message': 'Role Not supported.'}, status=status.HTTP_400_BAD_REQUEST)       	
			else:
				return JsonResponse({'message': 'User already exists.'}, status=status.HTTP_400_BAD_REQUEST) 
		else:
			return JsonResponse({'message': 'Check the registration details, not valid.'}, status=status.HTTP_400_BAD_REQUEST)  

#============================================================================================
# Login 
#============================================================================================
@api_view(['GET'])
def LoginAPI(request):
	if request.method == 'GET':
		user_id = request.query_params.get('user_id', None)
		user_password = request.query_params.get('user_password', None)
		user_role = request.query_params.get('user_role', None)

		# user_data = JSONParser().parse(request)
		# user_id = user_data['user_id']
		# user_password = user_data['user_password']	
		# user_role = user_data['user_role']	

		if user_id is not None and user_password is not None and user_role is not None:	
			users = AppUser.objects.all()
			users = users.filter(user_id__icontains=user_id) 	
			users = users.filter(user_password__icontains=user_password) 	
			users = users.filter(user_role__icontains=user_role) 
			if(len(users) != 0):
				if (user_role == "1" or user_role == "2"):
					serializer = AppUserSerializer(users, many=True)
					res = JsonResponse(serializer.data, safe=False)
					return res
				else:
					return JsonResponse({'message': 'Role Not supported.'}, status=status.HTTP_204_NO_CONTENT)       	
			else:
				return JsonResponse({'message': 'Invalid credentials, try again.'}, status=status.HTTP_204_NO_CONTENT)       
		else:
			return JsonResponse({'message': 'Invalid input, please check.'}, status=status.HTTP_204_NO_CONTENT)  

#============================================================================================
# Change password 
#============================================================================================
@api_view(['PUT'])
def ChangePasswordAPI(request):
	if request.method == 'PUT':
		user_data = JSONParser().parse(request)

		user_id = user_data['user_id']
		user_new_password = user_data['user_new_password']	

		if user_id is not None:
			users = AppUser.objects.all()
			users = users.filter(user_id__icontains=user_id)		
			
			if(len(users) == 1):
				obj = AppUser.objects.get(pk=users[0].id)
				obj.user_password = user_new_password
				obj.save()
				return JsonResponse({'message': 'Password updated successfully.'}, status=status.HTTP_200_OK)
			else:
				return JsonResponse({'message': 'Invalid credentials, try again.'}, status=status.HTTP_204_NO_CONTENT)       
		else:
			return JsonResponse({'message': 'Invalid input, please check.'}, status=status.HTTP_204_NO_CONTENT) 