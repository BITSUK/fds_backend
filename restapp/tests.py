from django.test import TestCase
from rest_framework.test import RequestsClient
from rest_framework.test import APITestCase
from rest_framework import status

class BasicTests(APITestCase):

    # Admin panel is up
    def test01 (self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/admin')
        assert response.status_code == 200

    # Get Trains    
    def test02 (self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/fds/rest/api/trains')
        assert response.status_code == 200

    # Get Stations    
    def test03 (self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/fds/rest/api/stations/')
        assert response.status_code == 200