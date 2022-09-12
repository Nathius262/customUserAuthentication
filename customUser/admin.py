from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin
from customUser.models import User

class UserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_staff', 'is_active')
    search_fields = ('email', 'username', 'name')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, UserAdmin)