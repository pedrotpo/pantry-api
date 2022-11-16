from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("email",)
    search_fields = ("email",)
    fieldsets = (
        (
            _("General"),
            {
                "fields": (
                    "email",
                    "password",
                    "created",
                    "last_login",
                )
            },
        ),
        (_("Profile"), {"fields": (("first_name", "last_name"),)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_superuser",
                    "is_staff",
                )
            },
        ),
        (_("Groups"), {"fields": ("groups",)}),
    )
    readonly_fields = (
        "created",
        "last_login",
    )
