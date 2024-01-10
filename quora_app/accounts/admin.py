from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from django.contrib.auth.forms import UserChangeForm, UserCreationForm

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = (
        "email",
        "username",
        "is_staff",
        "is_active",
    )


# Register your models here.

admin.site.register(CustomUser, CustomUserAdmin)
