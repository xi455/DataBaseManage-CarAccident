from django.db import models

from transport_subsidiary.models import UnitName, VehicleType
from django.db.models.signals import post_delete
from django.dispatch import receiver

class AccidentRecords(models.Model):
    id = models.AutoField(primary_key=True)
    發生年度 = models.CharField(max_length=4, null=True)
    發生月份 = models.CharField(max_length=2, null=True)
    發生日期 = models.CharField(max_length=8, null=True)
    發生時間 = models.CharField(max_length=6, null=True)
    class AccidentType(models.TextChoices):
        FIRST_ACCIDENTTYPE = "A1", "A1"
        SECOND_ACCIDENTTYPE = "A2", "A2"


    # 事故類別名稱 = models.CharField(
    #     max_length=2, choices=AccidentType.choices, default=AccidentType.FIRST_ACCIDENTTYPE
    # )
    處理單位名稱警局層 = models.ForeignKey(UnitName, models.DO_NOTHING, db_column='處理單位名稱警局層', null=True)
    發生地點 = models.CharField(max_length=80, null=True)
    class AccidentType(models.TextChoices):
        FIRST_ACCIDENTTYPE = "A1", "A1"
        SECOND_ACCIDENTTYPE = "A2", "A2"

    class WeatherType(models.TextChoices):
        FIRST_WEATHERTYPE = "晴", "晴"
        SECOND_WEATHERTYPE = "雪", "雪"
        THIRD_WEATHERTYPE = "風沙", "風沙"
        FOURTH_WEATHERTYPE = "暴雨", "暴雨"
        FIFTH_WEATHERTYPE = "強風", "強風"
        SIXTH_WEATHERTYPE = "雨", "雨"
        SEVENTH_WEATHERTYPE = "陰", "陰"
        EIGHTH_WEATHERTYPE = "霧或煙", "霧或煙"

    天候名稱 = models.CharField(
        max_length=10, choices=WeatherType.choices, default=WeatherType.FIRST_WEATHERTYPE
    )
    class LightType(models.TextChoices):
        FIRST_LIGHTTYPE = "夜間(或隧道、地下道、涵洞)有照明", "夜間(或隧道、地下道、涵洞)有照明"
        SECOND_LIGHTTYPE = "夜間(或隧道、地下道、涵洞)無照明", "夜間(或隧道、地下道、涵洞)無照明"
        THIRD_LIGHTTYPE = "有照明未開啟或故障", "有照明未開啟或故障"
        FORTH_LIGHTTYPE = "晨或暮光", "晨或暮光"
        FIFTH_LIGHTTYPE = "日間自然光線", "日間自然光線"

    光線名稱 = models.CharField(
        max_length=20, 
         choices=LightType.choices,
         default=LightType.FIRST_LIGHTTYPE
    )

    事故類別名稱 = models.CharField(
        max_length=2, choices=AccidentType.choices, default=AccidentType.FIRST_ACCIDENTTYPE
    )
    經度 = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    緯度 = models.DecimalField(max_digits=9, decimal_places=6, null=True)

    class Meta:
        verbose_name = "事故紀錄"
        verbose_name_plural = "事故紀錄"
        db_table_comment = "事故紀錄表"
        managed = True
        db_table = 'accident_records'

    def __str__(self):
        return str(int(self.pk))


class CauseAnalysis(models.Model):
    id = models.AutoField(primary_key=True)
    accident = models.ForeignKey(AccidentRecords, models.DO_NOTHING, blank=True, null=True)

    class BigCategoryNameJudgmentMain(models.TextChoices):
        FIRST_BIGCATEGORYNAMEJUDGMENTMAIN = "無(非車輛駕駛人因素)", "無(非車輛駕駛人因素)"
        SECOND_BIGCATEGORYNAMEJUDGMENTMAIN = "無(車輛駕駛人因素)", "無(車輛駕駛人因素)"
        THIRD_BIGCATEGORYNAMEJUDGMENTMAIN = "機件", "機件"
        FOURTH_BIGCATEGORYNAMEJUDGMENTMAIN = "裝載", "裝載"
        FIFTH_BIGCATEGORYNAMEJUDGMENTMAIN = "交通管制(設施)", "交通管制(設施)"
        SIXTH_BIGCATEGORYNAMEJUDGMENTMAIN = "燈光", "燈光"
        SEVENTH_BIGCATEGORYNAMEJUDGMENTMAIN = "駕駛人", "駕駛人"
        EIGHTH_BIGCATEGORYNAMEJUDGMENTMAIN = "行人(或乘客)", "行人(或乘客)"
        NINETH_BIGCATEGORYNAMEJUDGMENTMAIN = "其他", "其他"

    肇因研判大類別名稱_主要 = models.CharField(
        max_length=15, choices=BigCategoryNameJudgmentMain.choices, default=BigCategoryNameJudgmentMain.FIRST_BIGCATEGORYNAMEJUDGMENTMAIN
    )
    肇因研判子類別名稱_主要 = models.CharField(max_length=25, null=True)
    肇因研判子類別名稱_個別 = models.CharField(max_length=25, null=True)
    # class WhetherToEscape(models.TextChoices):
    #     FIRST_WHETHERTOESCAPE = "A1", "A1"
    #     SECOND_WHETHERTOESCAPE = "A2", "A2"


    # 肇事逃逸類別名稱_是否肇逃 = models.CharField(
    #     max_length=2, choices=WhetherToEscape.choices, default=WhetherToEscape.FIRST_WHETHERTOESCAPE
    # )

    肇事逃逸類別名稱_是否肇逃 = models.BooleanField(default=False)

    class Meta:
        verbose_name = "原因分析"
        verbose_name_plural = "原因分析"
        db_table_comment = "原因分析表"
        managed = True
        db_table = 'cause_analysis'

    def __str__(self):
        return self.肇因研判大類別名稱_主要


class PartyInfo(models.Model):
    id = models.AutoField(primary_key=True)
    accident = models.ForeignKey(AccidentRecords, models.DO_NOTHING, blank=True, null=True)
    當事者區分_類別_大類別名稱_車種 = models.ForeignKey(VehicleType, models.DO_NOTHING, db_column='當事者區分_類別_大類別名稱_車種', null=True)
    class Gender(models.TextChoices):
        FIRST_GENDER = "男", "男"
        SECOND_GENDER = "女", "女"
        THIRD_GENDER = "肇事逃逸尚未查獲", "肇事逃逸尚未查獲"
        FOURTH_GENDER = "無或物(動物、堆置物)", "無或物(動物、堆置物)"

    當事者性別名稱 = models.CharField(
        max_length=15, choices=Gender.choices, default=Gender.FIRST_GENDER
    )
    當事者事故發生時年齡 = models.IntegerField(null=True)
    class ProtectiveEquipment(models.TextChoices):
        FIRST_PROTECTIVEQUIPMENT = "無", "無"
        SECOND_PROTECTIVEQUIPMENT = (
            "未戴案全帽或未繫安全帶(未使用幼童安全椅)",
            "未戴案全帽或未繫安全帶(未使用幼童安全椅)",
        )
        THIRD_PROTECTIVEQUIPMENT = (
            "戴安全帽或繫安全帶(使用幼童安全椅)",
            "戴安全帽或繫安全帶(使用幼童安全椅)",
        )
        FOURTH_PROTECTIVEQUIPMENT = "其他(行人、慢車駕駛人)", "其他(行人、慢車駕駛人)"
        FIFTH_PROTECTIVEQUIPMENT = (
            "其他(無需使用保護裝備之人)",
            "其他(無需使用保護裝備之人)",
        )
        SIXTH_PROTECTIVEQUIPMENT = "不明", "不明"

    保護裝備名稱 = models.CharField(
        max_length=25,
        choices=ProtectiveEquipment.choices,
        default=ProtectiveEquipment.FIRST_PROTECTIVEQUIPMENT,
    )

    class ActionStatus(models.TextChoices):
        FIRST_ACTIONSTATUS = "無", "無"
        SECOND_ACTIONSTATUS = "向左變換車道", "向左變換車道"
        THIRD_ACTIONSTATUS = "倒車", "倒車"
        FOURTH_ACTIONSTATUS = "向右變換車道", "向右變換車道"
        FIFTH_ACTIONSTATUS = "超車(含超越)", "超車(含超越)"
        SIXTH_ACTIONSTATUS = "奔跑", "奔跑"
        SEVENTH_ACTIONSTATUS = "向前直行中", "向前直行中"
        EIGHTH_ACTIONSTATUS = "起步", "起步"
        NINETH_ACTIONSTATUS = "等待(引擎未熄火)", "等待(引擎未熄火)"
        TENTH_ACTIONSTATUS = "靜立(止)", "靜立(止)"
        ELEVENTH_ACTIONSTATUS = "上、下車", "上、下車"
        TWELFTH_ACTIONSTATUS = "迴轉或橫越道路中", "迴轉或橫越道路中"
        THIRTEENTH_ACTIONSTATUS = "急減速或急停止", "急減速或急停止"
        FOURTEENTH_ACTIONSTATUS = "右轉彎", "右轉彎"
        FIFTEENTH_ACTIONSTATUS = "插入行列", "插入行列"
        SIXTEENTH_ACTIONSTATUS = "步行", "步行"
        SEVENTEENTH_ACTIONSTATUS = "其他", "其他"
        EIGHTEENTH_ACTIONSTATUS = "停車操作中", "停車操作中"
        NINETEENTH_ACTIONSTATUS = "不明", "不明"
        TWENTIETH_ACTIONSTATUS = "靜止(引擎熄火)", "靜止(引擎熄火)"
        TWENTY_FIRST_ACTIONSTATUS = "左轉彎", "左轉彎"

    當事者行動狀態子類別名稱 = models.CharField(
        max_length=10,
        choices=ActionStatus.choices,
        default=ActionStatus.FIRST_ACTIONSTATUS,
    )

    class VehicleImpactPartSubcategoryNameInitial(models.TextChoices):
        FIRST_VEHICLEIMPACTPARTSUBCATEGORYNAMEINITIAL = "左前車頭(身)", "左前車頭(身)"
        SECOND_VEHICLEIMPACTPARTSUBCATEGORYNAMEINITIAL = "非汽(機)車", "非汽(機)車"
        THIRD_VEHICLEIMPACTPARTSUBCATEGORYNAMEINITIAL = "後車尾", "後車尾"
        FOURTH_VEHICLEIMPACTPARTSUBCATEGORYNAMEINITIAL = "左側車身", "左側車身"
        FIFTH_VEHICLEIMPACTPARTSUBCATEGORYNAMEINITIAL = "右後車尾(身)", "右後車尾(身)"
        SIXTH_VEHICLEIMPACTPARTSUBCATEGORYNAMEINITIAL = "車底", "車底"
        SEVENTH_VEHICLEIMPACTPARTSUBCATEGORYNAMEINITIAL = "不明", "不明"
        EIGHTH_VEHICLEIMPACTPARTSUBCATEGORYNAMEINITIAL = "右側車身", "右側車身"
        NINETH_VEHICLEIMPACTPARTSUBCATEGORYNAMEINITIAL = "車頂", "車頂"
        TENTH_VEHICLEIMPACTPARTSUBCATEGORYNAMEINITIAL = "右前車頭(身)", "右前車頭(身)"
        ELEVENTH_VEHICLEIMPACTPARTSUBCATEGORYNAMEINITIAL = "左後車尾(身)", "左後車尾(身)"
        TWELFTH_VEHICLEIMPACTPARTSUBCATEGORYNAMEINITIAL = "前車頭", "前車頭"


    車輛撞擊部位子類別名稱_最初 = models.CharField(max_length=10, choices=VehicleImpactPartSubcategoryNameInitial.choices, default=VehicleImpactPartSubcategoryNameInitial.FIRST_VEHICLEIMPACTPARTSUBCATEGORYNAMEINITIAL)

    class VehicleCategories(models.TextChoices):
        FIRST_VEHICLECATEGORIES = "無", "無"
        SECOND_VEHICLECATEGORIES = "機車", "機車"
        THIRD_VEHICLECATEGORIES = "汽車", "汽車"
        FOURTH_VEHICLECATEGORIES = "其他", "其他"

    車輛撞擊部位大類別名稱_其他 = models.CharField(
        max_length=25,
        choices=VehicleCategories.choices,
        default=VehicleCategories.FIRST_VEHICLECATEGORIES,
    )

    class VehicleImpactPartSubcategoryNameOther(models.TextChoices):
        FIRST_VEHICLEIMPACTPARTSUBCATEGORYNAMEOTHER = "左前車頭(身)", "左前車頭(身)"
        SECOND_VEHICLEIMPACTPARTSUBCATEGORYNAMEOTHER = "非汽(機)車", "非汽(機)車"
        THIRD_VEHICLEIMPACTPARTSUBCATEGORYNAMEOTHER = "後車尾", "後車尾"
        FOURTH_VEHICLEIMPACTPARTSUBCATEGORYNAMEOTHER = "左側車身", "左側車身"
        FIFTH_VEHICLEIMPACTPARTSUBCATEGORYNAMEOTHER = "右後車尾(身)", "右後車尾(身)"
        SIXTH_VEHICLEIMPACTPARTSUBCATEGORYNAMEOTHER = "車底", "車底"
        SEVENTH_VEHICLEIMPACTPARTSUBCATEGORYNAMEOTHER = "不明", "不明"
        EIGHTH_VEHICLEIMPACTPARTSUBCATEGORYNAMEOTHER = "右側車身", "右側車身"
        NINETH_VEHICLEIMPACTPARTSUBCATEGORYNAMEOTHER = "車頂", "車頂"
        TENTH_VEHICLEIMPACTPARTSUBCATEGORYNAMEOTHER = "右前車頭(身)", "右前車頭(身)"
        ELEVENTH_VEHICLEIMPACTPARTSUBCATEGORYNAMEOTHER = "左後車尾(身)", "左後車尾(身)"
        TWELFTH_VEHICLEIMPACTPARTSUBCATEGORYNAMEOTHER = "前車頭", "前車頭"

    車輛撞擊部位子類別名稱_其他 = models.CharField(max_length=10, choices=VehicleImpactPartSubcategoryNameOther.choices, default=VehicleImpactPartSubcategoryNameOther.FIRST_VEHICLEIMPACTPARTSUBCATEGORYNAMEOTHER)

    class Meta:
        verbose_name = "肇事人紀錄"
        verbose_name_plural = "肇事人紀錄"
        db_table_comment = "肇事人紀錄表"
        managed = True
        db_table = 'party_info'

    def __str__(self):
        return self.保護裝備名稱


class RoadConditions(models.Model):
    id = models.AutoField(primary_key=True)
    accident = models.ForeignKey(AccidentRecords, models.DO_NOTHING, blank=True, null=True)
    class BigRoadType(models.TextChoices):
        FIRST_BIGROADTYPE = "平交道", "平交道"
        SECOND_BIGROADTYPE = "單路部分", "單路部分"
        THIRD_BIGROADTYPE = "圓環廣場", "圓環廣場"
        FOURTH_BIGROADTYPE = "交岔路", "交岔路"

    道路型態大類別名稱 = models.CharField(
        max_length=4, choices=BigRoadType.choices, default=BigRoadType.FIRST_BIGROADTYPE
    )

    class SmallRoadType(models.TextChoices):
        FIRST_SMALLROADTYPE = "彎曲路及附近", "彎曲路及附近"
        SECOND_SMALLROADTYPE = "圓環", "圓環"
        THIRD_SMALLROADTYPE = "有遮斷器", "有遮斷器"
        FOURTH_SMALLROADTYPE = "涵洞", "涵洞"
        FIFTH_SMALLROADTYPE = "廣場", "廣場"
        SIXTH_SMALLROADTYPE = "三岔路", "三岔路"
        SEVENTH_SMALLROADTYPE = "地下道", "地下道"
        EIGHTH_SMALLROADTYPE = "高架道路", "高架道路"
        NINETH_SMALLROADTYPE = "直路", "直路"
        TENTH_SMALLROADTYPE = "坡路", "坡路"
        ELEVENTH_SMALLROADTYPE = "四岔路", "四岔路"
        TWELFTH_SMALLROADTYPE = "無遮斷器", "無遮斷器"
        THIRTEENTH_SMALLROADTYPE = "橋樑", "橋樑"
        FOURTEENTH_SMALLROADTYPE = "多岔路", "多岔路"
        FIFTEENTH_SMALLROADTYPE = "巷弄", "巷弄"
        SIXTEENTH_SMALLROADTYPE = "其他", "其他"
        SEVENTEENTH_SMALLROADTYPE = "隧道", "隧道"

    道路型態子類別名稱 = models.CharField(
        max_length=10,
        choices=SmallRoadType.choices,
        default=SmallRoadType.FIRST_SMALLROADTYPE,
    )

    class AccidentLocation(models.TextChoices):
        FIRST_ACCIDENTLOCATION = "路段", "路段"
        SECOND_ACCIDENTLOCATION = "交叉路口", "交叉路口"
        THIRD_ACCIDENTLOCATION = "交流道", "交流道"
        FOURTH_ACCIDENTLOCATION = "其他", "其他"

    事故位置大類別名稱 = models.CharField(
        max_length=4,
        choices=AccidentLocation.choices,
        default=AccidentLocation.FIRST_ACCIDENTLOCATION,
    )

    class RoadSurfacePaving(models.TextChoices):
        FIRST_ROADSURFACEPAVING = "柏油", "柏油"
        SECOND_ROADSURFACEPAVING = "碎石", "碎石"
        THIRD_ROADSURFACEPAVING = "水泥", "水泥"
        FOURTH_ROADSURFACEPAVING = "無鋪裝", "無鋪裝"
        FIFTH_ROADSURFACEPAVING = "其他鋪裝", "其他鋪裝"

    路面狀況_路面鋪裝名稱 = models.CharField(
        max_length=4,
        choices=RoadSurfacePaving.choices,
        default=RoadSurfacePaving.FIRST_ROADSURFACEPAVING,
    )

    class RoadSurfaceCondition(models.TextChoices):
        FIRST_ROADSURFACECONDITION = "濕潤", "濕潤"
        SECOND_ROADSURFACECONDITION = "冰雪", "冰雪"
        THIRD_ROADSURFACECONDITION = "油滑", "油滑"
        FOURTH_ROADSURFACECONDITION = "乾燥", "乾燥"
        FIFTH_ROADSURFACECONDITION = "泥濘", "泥濘"

    路面狀況_路面狀態名稱 = models.CharField(
        max_length=2,
        choices=RoadSurfaceCondition.choices,
        default=RoadSurfaceCondition.FIRST_ROADSURFACECONDITION,
    )

    class RoadSurfaceDefect(models.TextChoices):
        FIRST_ROADSURFACEDEFECT = "無缺陷", "無缺陷"
        SECOND_ROADSURFACEDEFECT = "路面鬆軟", "路面鬆軟"
        THIRD_ROADSURFACEDEFECT = "有坑洞", "有坑洞"
        FOURTH_ROADSURFACEDEFECT = "突出(高低)不平", "突出(高低)不平"

    路面狀況_路面缺陷名稱 = models.CharField(
        max_length=10,
        choices=RoadSurfaceDefect.choices,
        default=RoadSurfaceDefect.FIRST_ROADSURFACEDEFECT,
    )

    class RoadObstacle(models.TextChoices):
        FIRST_ROADOBSTACLE = "道路工事(程)中", "道路工事(程)中"
        SECOND_ROADOBSTACLE = "路上有停車", "路上有停車"
        THIRD_ROADOBSTACLE = "有堆積物", "有堆積物"
        FOURTH_ROADOBSTACLE = "無障礙物", "無障礙物"
        FIFTH_ROADOBSTACLE = "其他障礙物", "其他障礙物"

    道路障礙_障礙物名稱 = models.CharField(
        max_length=10,
        choices=RoadObstacle.choices,
        default=RoadObstacle.FIRST_ROADOBSTACLE,
    )

    class RoadblocksVisibilityQuality(models.TextChoices):
        FIRST_ROADBLOCKSVISIBILITYQUALITY = "無遮蔽", "無遮蔽"
        SECOND_ROADBLOCKSVISIBILITYQUALITY = "不良", "不良"
        THIRD_ROADBLOCKSVISIBILITYQUALITY = "良好", "良好"

    道路障礙_視距品質名稱 = models.CharField(
        max_length=10,
        choices=RoadblocksVisibilityQuality.choices,
        default=RoadblocksVisibilityQuality.FIRST_ROADBLOCKSVISIBILITYQUALITY,
    )

    class RoadblocksVisibility(models.TextChoices):
        FIRST_ROADBLOCKSVISIBILITY = "坡道", "坡道"
        SECOND_ROADBLOCKSVISIBILITY = "樹木、農作物", "樹木、農作物"
        THIRD_ROADBLOCKSVISIBILITY = "彎道", "彎道"
        FOURTH_ROADBLOCKSVISIBILITY = "路上停放車輛", "路上停放車輛"
        FIFTH_ROADBLOCKSVISIBILITY = "良好", "良好"
        SIXTH_ROADBLOCKSVISIBILITY = "建築物", "建築物"
        SEVENTH_ROADBLOCKSVISIBILITY = "其他", "其他"

    道路障礙_視距名稱 = models.CharField(
        max_length=10,
        choices=RoadblocksVisibility.choices,
        default=RoadblocksVisibility.FIRST_ROADBLOCKSVISIBILITY,
    )

    class Meta:
        verbose_name = "道路狀況"
        verbose_name_plural = "道路狀況"
        db_table_comment = "道路狀況表"
        managed = True
        db_table = 'road_conditions'

    def __str__(self):
        return self.道路型態大類別名稱


class TrafficFacilities(models.Model):
    id = models.AutoField(primary_key=True)
    accident = models.ForeignKey(AccidentRecords, models.DO_NOTHING, blank=True, null=True)
    class LogType(models.TextChoices):
        FIRST_LOGTYPE = "行車管制號誌", "行車管制號誌"
        SECOND_LOGTYPE = "無號誌", "無號誌"
        THIRD_LOGTYPE = "閃光號誌", "閃光號誌"
        FOURTH_LOGTYPE = (
            "行車管制號誌(附設行人專用號誌)",
            "行車管制號誌(附設行人專用號誌)",
        )

    號誌_號誌種類名稱 = models.CharField(
        max_length=20, choices=LogType.choices, default=LogType.FIRST_LOGTYPE
    )

    class LogAction(models.TextChoices):
        FIRST_LOGACTION = "無號誌", "無號誌"
        SECOND_LOGACTION = "無動作", "無動作"
        THIRD_LOGACTION = "正常", "正常"
        FOURTH_LOGACTION = "不正常", "不正常"

    號誌_號誌動作名稱 = models.CharField(
        max_length=3, choices=LogAction.choices, default=LogAction.FIRST_LOGACTION
    )

    class Meta:
        verbose_name = "交通設施"
        verbose_name_plural = "交通設施"
        db_table_comment = "交通設施表"
        managed = True
        db_table = 'traffic_facilities'

    def __str__(self):
        return self.號誌_號誌種類名稱
    
@receiver(post_delete, sender=AccidentRecords)
def delete_related_models(sender, instance, **kwargs):
    instance.partyinfo_set.all().delete()
    instance.causeanalysis_set.all().delete()
    instance.trafficfacilities_set.all().delete()
    instance.roadconditions_set.all().delete()