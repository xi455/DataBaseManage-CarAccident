from django.urls import path

from report import views

app_name = "report"
urlpatterns = [
    path("list/", views.ErrorReportListView.as_view(), name="list"),
    path("create/", views.ErrorReportCreateView.as_view(), name="create"),
    path("detail/<pk>/", views.ErrorReportDetailView.as_view(), name="detail"),
    
    path("detail/<pk>/repair/", views.CheckRepair, name="check_repair"),
    path("detail/<pk>/overrule/", views.CheckOverrule, name="check_overrule"),
]