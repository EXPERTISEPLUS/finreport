
from django.contrib import admin
from .models import (Firm, Company, Membership
)


# ========================
# CORE
# ========================

@admin.register(Firm)
class FirmAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "firm", "created_at")
    search_fields = ("name", "firm__name")
    list_filter = ("firm",)


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ("user", "company", "role")
    search_fields = ("user__username", "company__name")
    list_filter = ("role", "company")

