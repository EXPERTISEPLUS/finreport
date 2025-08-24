from django.contrib import admin
from .models import (Company, Exercise, Account, JournalEntry,
TrialBalance, Closure
)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "country", "currency")

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ("id", "company", "year", "start_date", "end_date", "is_closed")
    list_filter = ("company", "is_closed")

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "label", "nature")

@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ("id", "exercise", "description", "date")  
    list_filter = ("exercise", "date")

@admin.register(TrialBalance)
class TrialBalanceAdmin(admin.ModelAdmin):
    list_display = ("id", "exercise", "generated_on")

@admin.register(Closure)
class ClosureAdmin(admin.ModelAdmin):
    list_display = ("id", "exercise", "date_closed")
    list_filter = ("exercise",)
