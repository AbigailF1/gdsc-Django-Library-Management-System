from django.contrib import admin
from .models import Profile, AdminSignupRequest
# Register your models here.
admin.site.register(Profile)

class AdminSignupRequestAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'created_at']
    list_per_page = 5
    ordering = ['created_at']

admin.site.register(AdminSignupRequest, AdminSignupRequestAdmin)
