from django.contrib import admin
from .models import IssueHistory, Issues, Roles

admin.site.register(IssueHistory)
admin.site.register(Issues)
admin.site.register(Roles)
