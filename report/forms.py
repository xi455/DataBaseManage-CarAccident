from django import forms

from report.models import (
    ErrorReport
)


class ErrorReportForm(forms.ModelForm):
    class Meta:
        model = ErrorReport
        exclude = ["用戶", "回報日期", "處理狀態"]

        widgets = {
            "錯誤型態": forms.Select(attrs={"class": "form-select"}),
            "錯誤描述": forms.TextInput(attrs={"class": "form-control"}),
            "查詢內容": forms.TextInput(attrs={"class": "form-control"}),
            "錯誤頁面": forms.TextInput(attrs={"class": "form-control"}),
            "具體位置描述": forms.TextInput(attrs={"class": "form-control"}),
            "其他說明": forms.TextInput(attrs={"class": "form-control"}),
            "錯誤截圖": forms.FileInput(attrs={"class": "form-control", "type": "file", "accept": "image/*"}),
        }