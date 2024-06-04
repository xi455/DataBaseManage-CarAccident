from django.db import models

# Create your models here.


class UnitName(models.Model):
    處理單位名稱警局層 = models.CharField(max_length=10)

    class Meta:
        verbose_name = "處理單位名稱警局層"
        verbose_name_plural = "處理單位名稱警局層"
        db_table_comment = "處理單位名稱警局層表"

    def __str__(self):
        return self.處理單位名稱警局層


class VehicleType(models.Model):
    當事者區分_類別_大類別名稱_車種 = models.CharField(max_length=15)

    class Meta:
        verbose_name = "當事者區分_類別_大類別名稱_車種"
        verbose_name_plural = "當事者區分_類別_大類別名稱_車種"
        db_table_comment = "當事者區分_類別_大類別名稱_車種表"

    def __str__(self):
        return self.當事者區分_類別_大類別名稱_車種
