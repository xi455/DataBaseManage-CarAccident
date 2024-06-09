from django.contrib import admin

# Register your models here.
from report.models import ErrorReport


@admin.register(ErrorReport)
class ErrorReportAdmin(admin.ModelAdmin):
    list_display = ["用戶", "錯誤型態", "錯誤頁面", "回報日期", "處理狀態"]
    list_display_links = ["用戶", "錯誤型態", "錯誤頁面", "回報日期"]
    search_fields = ["用戶", "錯誤型態", "錯誤頁面", "回報日期", "處理狀態"]
    list_per_page = 20