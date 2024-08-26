from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.views import APIView

from .serializers import UserSerializer
from .authentication import *

from rest_framework import status
# Create your views here.

class RegisterView(APIView):
    def post(self,request):
        data = request.data
        
        if data['password'] != data['password_confirm']:
            raise exceptions.APIExceptions('password do not match')
        
        serializers = UserSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)


class LoginAPIView(APIView):
    def post(self,request):
        
        email = request.data['email']
        password = request.data['password']
        
        if not email or not password:
            return Response({"error": "Email and password are required"},
                              status=status.HTTP_400_BAD_REQUEST)
            
        user = authenticate(email = email, password = password)
        
        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)
        
        response = Response()
        
        response.set_cookie(key='refresh_token',value=refresh_token,httponly=True)
        
        response.data = {
            'token' : access_token
        }
        
        return response
                


        
        
        
        
        