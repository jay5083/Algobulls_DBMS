from django.shortcuts import render, redirect
from django.views import View
from base.views import index, home
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login    
from base.models import AlgobullsEmployee

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('username')  # Assuming 'username' corresponds to email
        password = request.POST.get('password')

        if email and password:
            try:
                user = AlgobullsEmployee.objects.get(email_id=email, password=password)
            except AlgobullsEmployee.DoesNotExist:
                user = None
            
            if user is not None:
                # Authentication successful
                # Fetch additional details of the user
               
                
                # Redirect to home view after successful authentication
                return redirect('base:home')
        
        # Redirect back to login page on authentication failure
        return redirect('login')
