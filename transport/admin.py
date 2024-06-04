from django.contrib import admin

import transport.models as transport_models

# Register your models here.


@admin.register(transport_models.AccidentRecords)
class AccidentRecordsAdmin(admin.ModelAdmin):
    list_display = [
        "發生年度",
        "發生月份",
        "發生日期",
        "發生時間",
        "事故類別名稱",
        "處理單位名稱警局層",
        "發生地點",
    ]
    list_display_links = [
        "發生年度",
        "發生月份",
        "發生日期",
        "發生時間",
        "事故類別名稱",
        "處理單位名稱警局層",
        "發生地點",
    ]
    search_fields = [
        "發生年度",
        "發生月份",
        "發生日期",
        "發生時間",
        "事故類別名稱",
        "處理單位名稱警局層",
        "發生地點",
    ]
    list_per_page = 20


@admin.register(transport_models.PartyInfo)
class PartyInfoAdmin(admin.ModelAdmin):
    list_display = [
        "當事者性別名稱",
        "當事者事故發生時年齡",
    ]
    list_display_links = [
        "當事者性別名稱",
        "當事者事故發生時年齡",
    ]
    search_fields = [
        "當事者性別名稱",
        "當事者事故發生時年齡",
    ]
    list_per_page = 20


@admin.register(transport_models.CauseAnalysis)
class CauseAnalysisAdmin(admin.ModelAdmin):
    list_display = [
        "肇因研判大類別名稱_主要",
        "肇因研判子類別名稱_主要",
        "肇因研判子類別名稱_個別",
        "肇事逃逸類別名稱_是否肇逃",
    ]
    list_display_links = [
        "肇因研判大類別名稱_主要",
        "肇因研判子類別名稱_主要",
        "肇因研判子類別名稱_個別",
        "肇事逃逸類別名稱_是否肇逃",
    ]
    search_fields = [
        "肇因研判大類別名稱_主要",
        "肇因研判子類別名稱_主要",
        "肇因研判子類別名稱_個別",
        "肇事逃逸類別名稱_是否肇逃",
    ]
    list_per_page = 20


@admin.register(transport_models.TrafficFacilities)
class TrafficFacilitiesAdmin(admin.ModelAdmin):
    list_display = ["accident_id", "號誌_號誌種類名稱", "號誌_號誌動作名稱"]
    list_display_links = ["accident_id", "號誌_號誌種類名稱", "號誌_號誌動作名稱"]
    search_fields = ["accident_id", "號誌_號誌種類名稱", "號誌_號誌動作名稱"]
    list_per_page = 20


@admin.register(transport_models.RoadConditions)
class RoadConditionsAdmin(admin.ModelAdmin):
    list_display = ["道路型態子類別名稱", "道路型態大類別名稱", "事故位置大類別名稱"]
    list_display_links = [
        "道路型態子類別名稱",
        "道路型態大類別名稱",
        "事故位置大類別名稱",
    ]
    search_fields = ["道路型態子類別名稱", "道路型態大類別名稱", "事故位置大類別名稱"]
    list_per_page = 20
