from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

class RegisterView(APIView):
    permission_classes = [AllowAny]   # 👈 VERY IMPORTANT

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )

        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
