from typing import Iterable
from django.db import models
from django.urls import reverse
from users.models import User

# Create your models here.
class ErrorReport(models.Model):

    用戶 = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用戶")

    class ErrorType(models.TextChoices):
        FIRST_ERRORTYPE = "資料不正確", "資料不正確"
        SECOND_ERRORTYPE = "資料遺漏", "資料遺漏"
        THIRD_ERRORTYPE = "系統錯誤", "系統錯誤"
        FOURTH_ERRORTYPE = "圖表錯誤", "圖表錯誤"
        FIFTH_ERRORTYPE = "其他", "其他"
    
    錯誤型態 = models.CharField(max_length=5, choices=ErrorType.choices, default=ErrorType.FIRST_ERRORTYPE, verbose_name="錯誤類型")
    錯誤描述 = models.TextField(verbose_name="錯誤描述")

    查詢內容 = models.CharField(max_length=200, verbose_name="查詢內容", blank=True, null=True)

    錯誤頁面 = models.CharField(max_length=200, verbose_name="錯誤發現於哪個頁面或功能")
    具體位置描述 = models.TextField(verbose_name="具體位置描述", blank=True, null=True)

    錯誤截圖 = models.ImageField(upload_to='error_screenshots/', verbose_name="錯誤截圖", blank=True, null=True)
    其他說明 = models.TextField(verbose_name="其他說明", blank=True, null=True)

    回報日期 = models.DateTimeField(auto_now_add=True, verbose_name="回報日期")

    class CheckHandle(models.TextChoices):
        FIRST_CHECKHANDLE = "未處理", "未處理"
        SECOND_CHECKHANDLE = "已處理", "已處理"
        THIRD_CHECKHANDLE = "駁回", "駁回"

    處理狀態 = models.CharField(max_length=5, choices=CheckHandle.choices, default=CheckHandle.FIRST_CHECKHANDLE, verbose_name="處理狀態")

    def __str__(self):
        return f"{self.用戶} - {self.錯誤型態} - {self.查詢內容}"
    
    def get_absolute_url(self):
        return reverse("user_profile", kwargs={"pk": self.用戶.id})
        
    class Meta:
        verbose_name = "錯誤回報"
        verbose_name_plural = "錯誤回報"