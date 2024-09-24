from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'phone_number', 'email', 'gender','password')
admin.site.register(User, UserAdmin)