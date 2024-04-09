from django.shortcuts import render, redirect, reverse
from django.views import View
from base.views import index, home
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login    
from base.models import AlgobullsEmployee, Roles, BrokerSideEmployee

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
        
    def post(self, request):
        email = request.POST.get('username')  # Assuming 'username' corresponds to email
        password = request.POST.get('password')
        
        if email and password:
            # Check in AlgobullsEmployee table
            try:
                user = AlgobullsEmployee.objects.get(email_id=email, password=password)
            except AlgobullsEmployee.DoesNotExist:
                user = None
            
            if user is None:
                # If user not found in AlgobullsEmployee table, check in BrokerSideEmployee table
                try:
                    broker_user = BrokerSideEmployee.objects.get(email_id=email, password=password)
                except BrokerSideEmployee.DoesNotExist:
                    broker_user = None
                
                if broker_user is not None:
                    employee_id = broker_user.employee_id
                    role_name = broker_user.role_id.role_name if broker_user.role_id else None
                    name = broker_user.name
                    # Authentication successful
                    # Redirect to home page with employee_id and role_name
                    return redirect('base:home', employee_id=employee_id, role_name=role_name, name=name)
            else:
                # If user found in AlgobullsEmployee table
                employee_id = user.employee_id
                role_name = user.role_id.role_name if user.role_id else None
                name = user.name
                print(name)
                # Authentication successful
                # Redirect to home page with employee_id and role_name
                return redirect('base:home', employee_id=employee_id, role_name=role_name, name=name)
                
        # Redirect back to login page on authentication failure
        return redirect('login')
