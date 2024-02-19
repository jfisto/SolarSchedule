from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from models import Users
from .forms import UsersCreationForm, UsersChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = UsersCreationForm
    form = UsersChangeForm
    model = Users
    list_display = ('email', 'username', 'status', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('email', 'username', 'status', 'is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        (None,
         {'fields': ('email', 'username', 'password', 'status', 'first_name', 'last_name')}),
        ('Разрешения', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    readonly_fields = ('id',)


admin.site.register(Users, CustomUserAdmin)
