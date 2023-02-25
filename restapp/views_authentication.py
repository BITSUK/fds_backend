from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

import json

from restapp.models import AppUser
from restapp.serializers import AppUserSerializer

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

		if user_id is not None and user_name is not None and user_role is not None and user_password is not None:	
			users = AppUser.objects.all()
			users = users.filter(user_id__icontains = user_id) 		
			
			if(len(users) == 0):										# Check if user already exists
				if (user_email is None):								# Validate email, pending
					if (user_role == "1" or user_role == "2"):			# Validate role
						serializer = AppUserSerializer(data=new_user_data)					

						# OK
						if serializer.is_valid():
							serializer.save()
							return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 
						# NOT OK
						return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
					
					else:
						return JsonResponse({'message': 'Role Not supported.'}, status=status.HTTP_204_NO_CONTENT)       	
				else:
					JsonResponse({'message': 'Invalid email.'}, status=status.HTTP_204_NO_CONTENT)  
			else:
				return JsonResponse({'message': 'User already exists.'}, status=status.HTTP_204_NO_CONTENT)       
		else:
			return JsonResponse({'message': 'Check the registration details, not valid.'}, status=status.HTTP_204_NO_CONTENT)  

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
		user_old_password = user_data['user_old_password']	
		user_role = user_data['user_role']	

		if user_id is not None and user_role is not None:
			users = AppUser.objects.all()
			users = users.filter(user_id__icontains=user_id)		
			users = users.filter(user_password__icontains=user_old_password)
			users = users.filter(user_role__icontains=user_role)
			
			if(len(users) == 1):
				serializer = AppUserSerializer(users, many=True)
				return JsonResponse(serializer.data, safe=False)
			else:
				return JsonResponse({'message': 'Invalid credentials, try again.'}, status=status.HTTP_204_NO_CONTENT)       
		else:
			return JsonResponse({'message': 'Invalid input, please check.'}, status=status.HTTP_204_NO_CONTENT) 