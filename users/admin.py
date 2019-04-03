from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import DB2UserCreationForm, DB2UserChangeForm
from .models import DB2User


class CustomUserAdmin(UserAdmin):
    add_form = DB2UserCreationForm
    form = DB2UserChangeForm
    model = DB2User
    list_display = ['email', 'username', ]

admin.site.register(DB2User, CustomUserAdmin)
