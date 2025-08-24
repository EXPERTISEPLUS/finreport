from django.contrib import admin
from .models import (ReportTemplate, ReportLine, MappingAccountReport, FinancialStatement
)



# ========================
# REPORTING
# ========================

class ReportLineInline(admin.TabularInline):
    model = ReportLine
    extra = 1


@admin.register(ReportTemplate)
class ReportTemplateAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "created_at")
    search_fields = ("name", "type")
    list_filter = ("type",)
    inlines = [ReportLineInline]


@admin.register(ReportLine)
class ReportLineAdmin(admin.ModelAdmin):
    list_display = ("template", "code", "label", "position")
    search_fields = ("label", "code", "template__name")
    list_filter = ("template",)


@admin.register(MappingAccountReport)
class MappingAccountReportAdmin(admin.ModelAdmin):
    list_display = ("account", "report_line")
    search_fields = ("account__number", "report_line__label")
    list_filter = ("report_line__template",)


@admin.register(FinancialStatement)
class FinancialStatementAdmin(admin.ModelAdmin):
    list_display = ("exercise", "template", "generated_on")
    search_fields = ("exercise__year", "template__name")
    list_filter = ("template", "exercise")

