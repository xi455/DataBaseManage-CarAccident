from django.contrib import admin

from transport_subsidiary.models import UnitName, VehicleType

# Register your models here.


@admin.register(UnitName)
class UnitNameAdmin(admin.ModelAdmin):
    list_display = ["處理單位名稱警局層"]
    list_display_links = ["處理單位名稱警局層"]
    search_fields = ["處理單位名稱警局層"]
    list_per_page = 20


@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ["當事者區分_類別_大類別名稱_車種"]
    list_display_links = ["當事者區分_類別_大類別名稱_車種"]
    search_fields = ["當事者區分_類別_大類別名稱_車種"]
    list_per_page = 20
