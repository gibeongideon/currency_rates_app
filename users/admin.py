from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class DuserAdmin(UserAdmin):

    list_display = (
        'id', 'username','email', 'first_name', 'last_name','last_login',)
    list_display_links = ('id',)
    search_fields = ('id',)
    ordering = ('id',)
    readonly_fields = ('password',)


admin.site.register(User, DuserAdmin)
