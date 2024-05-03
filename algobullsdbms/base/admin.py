from django.contrib import admin
from .models import IssueHistory, Issues, Roles, SalesLeads, AlgobullsDivision, AlgobullsEmployee, Branch, BrokerSideEmployee, Brokers, Permission, PermissionAccessTable
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.register(IssueHistory)
admin.site.register(Issues)
admin.site.register(Roles)
admin.site.register(SalesLeads)
admin.site.register(AlgobullsDivision)
admin.site.register(AlgobullsEmployee)
admin.site.register(Branch)
admin.site.register(BrokerSideEmployee)
admin.site.register(Brokers)
admin.site.register(Permission)
admin.site.register(PermissionAccessTable)

from django.contrib import admin
from django.contrib.auth.models import User, Permission
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import SalesLeads

# Unregister the default User admin
admin.site.unregister(User)

# Define a custom User admin
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username', 'email', 'first_name', 'last_name',)
    ordering = ('username',)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Fetch all the field names of the SalesLeads model
        sales_leads_fields = [field.name for field in SalesLeads._meta.fields]
        # Generate permissions for each field
        sales_leads_permissions = [
            (f"edit_{field}", f"Can edit the {field} field of Sales Leads") for field in sales_leads_fields
        ]
        # Get the IDs of the generated permissions
        sales_leads_perm_ids = [perm[0] for perm in sales_leads_permissions]
        # Filter permissions queryset
        filtered_permissions = Permission.objects.filter(codename__in=sales_leads_perm_ids)
        # Add the custom permissions to the user permissions field
        form.base_fields['user_permissions'].queryset = filtered_permissions
        return form

# Register the custom User admin
admin.site.register(User, UserAdmin)