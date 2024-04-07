from django.urls import path, include
from .views import authView, home, index, support_head_view, support_employee_view, update_employee_assigned_to, update_priority, update_comments, sales_leads, update_category, update_sales_leads
from . import views

urlpatterns = [
    path('', home, name='home'),
    path("signup/", authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', views.index, name='index'),
    path('support_head/', support_head_view, name='support_head'),  # View for Support Head
    path('support_employee/', support_employee_view, name='support_employee'),  # View for Support Employee
    path('update_employee_assigned_to/', update_employee_assigned_to, name='update_employee_assigned_to'),
    path('update_priority/', update_priority, name='update_priority'),
    path('update_comments/', update_comments, name='update_comments'),
    path('sales_leads/', sales_leads, name='sales_leads'),
    path('update_category/', update_category, name='update_category'),
    path('update_sales_leads/', update_sales_leads, name='update_sales_leads'),
]

