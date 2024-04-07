from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Roles, IssueHistory, Issues, AlgobullsEmployee, SalesLeads
from django.http import JsonResponse
import json
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from base.models import AlgobullsEmployee

def home(request):
    roles = Roles.objects.all()  # Fetch all roles
    issue_histories = IssueHistory.objects.all()
    issues = Issues.objects.all()
    sales_leads = SalesLeads.objects.all()
    
    return render(request, "base.html", {
        "roles": roles,
        "issue_histories": issue_histories,
        "issues": issues,
        "sales_leads": sales_leads,
    })

def authView(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "registration/login.html", {"form": form})

def index(request):
    roles = Roles.objects.all()  # Fetch all roles
    issue_histories = IssueHistory.objects.all()
    issues = Issues.objects.all()
    sales_leads = SalesLeads.objects.all()
    return render(request, "base.html", {"roles": roles, "issue_histories": issue_histories, "issues": issues, 'sales_leads': sales_leads})

def support_head_view(request):
    # Fetch data for Support Head
    roles = Roles.objects.all()  # Fetch all roles
    issue_histories = IssueHistory.objects.all()
    issues = Issues.objects.all()
    return render(request, "base.html", {"roles": roles, "issue_histories": issue_histories, "issues": issues})

def support_employee_view(request):
    # Fetch data for Support Employee
    issues = Issues.objects.all()
    return render(request, "base.html", {"issues": issues})

def update_employee_assigned_to(request):
    if request.method == 'POST':
        updated_values_json = request.POST.get('updated_values')
        updated_values = json.loads(updated_values_json)

        success_count = 0
        error_count = 0

        # Update records in the database based on the received data
        for issue_id, employee_id in updated_values.items():
            try:
                issue = Issues.objects.get(issue_id=issue_id)
                employee = AlgobullsEmployee.objects.get(pk=employee_id)
                issue.employee_assigned_to = employee
                issue.save()
                success_count += 1
            except (Issues.DoesNotExist, AlgobullsEmployee.DoesNotExist):
                error_count += 1

        return JsonResponse({'success_count': success_count, 'error_count': error_count})
    else:
        return JsonResponse({'error': 'Invalid request method'})

def update_priority(request):
    if request.method == 'POST':
        updated_priorities_json = request.POST.get('updated_priorities')
        updated_priorities = json.loads(updated_priorities_json)

        success_count = 0
        error_count = 0

        # Update records in the database based on the received data
        for issue_id, new_value in updated_priorities.items():
            try:
                issue = Issues.objects.get(issue_id=issue_id)
                issue.priority = new_value
                issue.save()
                success_count += 1
            except Issues.DoesNotExist:
                error_count += 1

        return JsonResponse({'success_count': success_count, 'error_count': error_count})
    else:
        return JsonResponse({'error': 'Invalid request method'})

def update_comments(request):
    if request.method == 'POST':
        updated_comments_json = request.POST.get('updated_comments')
        updated_comments = json.loads(updated_comments_json)

        success_count = 0
        error_count = 0

        for issue_id, new_comment in updated_comments.items():
            try:
                issue = Issues.objects.get(issue_id=issue_id)
                issue.comment = new_comment
                issue.save()
                success_count += 1
            except Issues.DoesNotExist:
                error_count += 1

        return JsonResponse({'success_count': success_count, 'error_count': error_count})
    else:
        return JsonResponse({'error': 'Invalid request method'})
    
def sales_leads(request):
    sales_leads = SalesLeads.objects.all()
    return render(request, 'sales_leads.html', {'sales_leads': sales_leads})

def update_category(request):
    if request.method == 'POST':
        updated_categories_json = request.POST.get('updated_categories')
        updated_categories = json.loads(updated_categories_json)

        success_count = 0
        error_count = 0

        # Update records in the database based on the received data
        for lead_id, new_category in updated_categories.items():
            try:
                lead = SalesLeads.objects.get(lead_id=lead_id)
                lead.category = new_category
                lead.save()
                success_count += 1
            except SalesLeads.DoesNotExist:
                error_count += 1

        return JsonResponse({'success_count': success_count, 'error_count': error_count})
    else:
        return JsonResponse({'error': 'Invalid request method'})

def update_sales_leads(request):
    if request.method == 'POST':
        updated_data_json = request.POST.get('updated_data')
        updated_data = json.loads(updated_data_json)

        success_count = 0
        error_count = 0

        # Update records in the database based on the received data
        for lead_id, lead_data in updated_data.items():
            try:
                lead = SalesLeads.objects.get(lead_id=lead_id)
                for field, value in lead_data.items():
                    setattr(lead, field, value)
                lead.save()
                success_count += 1
            except SalesLeads.DoesNotExist:
                error_count += 1

        return JsonResponse({'success_count': success_count, 'error_count': error_count})
    else:
        return JsonResponse({'error': 'Invalid request method'})



def create_new_entry(request):
    if request.method == 'POST':
        # Extract data from the POST request
        priority = request.POST.get('priority')
        comment = request.POST.get('comment')
        customer_name = request.POST.get('customer_name')
        number = request.POST.get('number')
        broking_id = request.POST.get('broking_id')
        email_id = request.POST.get('email_id')
        strategy_code = request.POST.get('strategy_code')
        strategy_instrument = request.POST.get('strategy_instrument')
        customer_type = request.POST.get('customer_type')
        issue = request.POST.get('issue')

        # Create a new entry in the Issues table
        new_entry = Issues.objects.create(
            priority=priority,
            comment=comment,
            customer_name=customer_name,
            number=number,
            broking_id=broking_id,
            email_id=email_id,
            strategy_code=strategy_code,
            strategy_instrument=strategy_instrument,
            customer_type=customer_type,
            issue=issue
            # Add other fields here if needed
        )

        # Return a success response
        return JsonResponse({'success': True})

    # If the request method is not POST, return an error response
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

