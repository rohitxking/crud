from django.contrib import admin
from .models import StudentModel

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','cls','city']

admin.site.register(StudentModel,StudentAdmin)