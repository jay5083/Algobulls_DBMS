from django.urls import path, include
from .views import  home,home1, index, support_head_view, support_employee_view, update_employee_assigned_to, update_priority, update_comments, sales_leads, update_category, update_sales_leads, update_issues
from . import views

urlpatterns = [
    path('<int:employee_id>/<str:role_name>/<str:name>/', home1, name='home1'),  
    path("accounts/", include("django.contrib.auth.urls")),
    path('accounts/profile/', home, name='home'),
    path('support_head/', support_head_view, name='support_head'),  # View for Support Head
    path('support_employee/', support_employee_view, name='support_employee'),  # View for Support Employee
    path('update_employee_assigned_to/', update_employee_assigned_to, name='update_employee_assigned_to'),
    path('update_priority/', update_priority, name='update_priority'),
    path('update_comments/', update_comments, name='update_comments'),
    path('sales_leads/', sales_leads, name='sales_leads'),
    path('update_category/', update_category, name='update_category'),
    path('update_sales_leads/', update_sales_leads, name='update_sales_leads'),
    path('update_issues/', update_issues, name='update_issues'),
]

