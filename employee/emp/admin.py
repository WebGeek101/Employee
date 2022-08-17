from django.contrib import admin

from .models import Department, Employee, role

# Register your models here.
admin.site.register(Employee)
admin.site.register(role)
admin.site.register(Department)
