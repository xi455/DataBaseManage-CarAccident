from django.db import models

# Create your models here.


class UnitName(models.Model):
    id = models.IntegerField(primary_key=True)
    處理單位名稱警局層 = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name = "處理單位名稱警局層"
        verbose_name_plural = "處理單位名稱警局層"
        db_table_comment = "處理單位名稱警局層表"

        managed = True
        db_table = 'unit_name'

    def __str__(self):
        return self.處理單位名稱警局層


class VehicleType(models.Model):
    id = models.IntegerField(primary_key=True)
    當事者區分_類別_大類別名稱_車種 = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        verbose_name = "當事者區分_類別_大類別名稱_車種"
        verbose_name_plural = "當事者區分_類別_大類別名稱_車種"
        db_table_comment = "當事者區分_類別_大類別名稱_車種表"

        managed = True
        db_table = 'vehicle_type'

    def __str__(self):
        return self.當事者區分_類別_大類別名稱_車種