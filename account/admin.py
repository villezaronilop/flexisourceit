from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


User = get_user_model()

# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = (
        "id",
        "username",
        "display_name",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "last_login",
    )
    fieldsets = (
        (
            "Personal info",
            {
                "fields": (
                    "id",
                    "first_name",
                    "last_name",
                    "username",
                    "display_name",
                    "email",
                )
            },
        ),
        (
            "Permissions",
            {"fields": ("is_active", "is_staff", "is_superuser", "groups")},
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    readonly_fields = ("id",)
    ordering = ["-date_joined"]

admin.site.register(User, CustomUserAdmin)
