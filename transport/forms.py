from django import forms

from transport.models import (
    AccidentRecords,
    PartyInfo,
    CauseAnalysis,
    TrafficFacilities,
    RoadConditions,
)

from transport_subsidiary.models import VehicleType


class AccidentRecordsForm(forms.ModelForm):
    class Meta:
        model = AccidentRecords
        fields = "__all__"

        widgets = {
            "發生年度": forms.TextInput(attrs={"class": "form-control"}),
            "發生月份": forms.TextInput(attrs={"class": "form-control"}),
            "發生日期": forms.TextInput(attrs={"class": "form-control"}),
            "發生時間": forms.TextInput(attrs={"class": "form-control"}),
            "事故類別名稱": forms.Select(attrs={"class": "form-select"}),
            "處理單位名稱警局層": forms.Select(attrs={"class": "form-select"}),
            "發生地點": forms.TextInput(attrs={"class": "form-control"}),
            "天候名稱": forms.Select(attrs={"class": "form-select"}),
            "光線名稱": forms.Select(attrs={"class": "form-select"}),
            "經度": forms.NumberInput(attrs={"class": "form-control"}),
            "緯度": forms.NumberInput(attrs={"class": "form-control"}),
        }


class PartyInfoForm(forms.ModelForm):
    class Meta:
        model = PartyInfo
        fields = "__all__"
        exclude = ["accident_id"]

        widgets = {
            "當事者區分_類別_大類別名稱_車種": forms.Select(attrs={"class": "form-select"}),
            "當事者性別名稱": forms.Select(attrs={"class": "form-select"}),
            "當事者事故發生時年齡": forms.NumberInput(attrs={"class": "form-control", 'min': '0', 'step': '1'}),
            "保護裝備名稱": forms.Select(attrs={"class": "form-select"}),
            "當事者行動狀態子類別名稱": forms.Select(attrs={"class": "form-select"}),
            "車輛撞擊部位子類別名稱_最初": forms.Select(attrs={"class": "form-select"}),
            "車輛撞擊部位大類別名稱_其他": forms.Select(attrs={"class": "form-select"}),
            "車輛撞擊部位子類別名稱_其他": forms.Select(attrs={"class": "form-select"}),
        }

    def __init__(self, *args, **kwargs):
        super(PartyInfoForm, self).__init__(*args, **kwargs)
        # self.fields['當事者區分_類別_大類別名稱_車種'].initial = VehicleType.objects.first()


class CauseAnalysisForm(forms.ModelForm):
    class Meta:
        model = CauseAnalysis
        fields = "__all__"
        exclude = ["accident_id"]

        widgets = {
            "肇因研判大類別名稱_主要": forms.TextInput(attrs={"class": "form-control"}),
            "肇因研判子類別名稱_主要": forms.TextInput(attrs={"class": "form-control"}),
            "肇因研判子類別名稱_個別": forms.TextInput(attrs={"class": "form-control"}),
            "肇事逃逸類別名稱_是否肇逃": forms.TextInput(attrs={"class": "form-control"}),
        }

class TrafficFacilitiesForm(forms.ModelForm):
    class Meta:
        model = TrafficFacilities
        fields = "__all__"
        exclude = ["accident_id"]
        
        widgets = {
            "號誌_號誌種類名稱": forms.Select(attrs={"class": "form-select"}),
            "號誌_號誌動作名稱": forms.Select(attrs={"class": "form-select"}),
        }


class RoadConditionsForm(forms.ModelForm):
    class Meta:
        model = RoadConditions
        fields = "__all__"
        exclude = ["accident_id"]

        widgets = {
            "道路型態大類別名稱": forms.Select(attrs={"class": "form-select"}),
            "道路型態子類別名稱": forms.Select(attrs={"class": "form-select"}),
            "事故位置大類別名稱": forms.Select(attrs={"class": "form-select"}),
            "路面狀況_路面鋪裝名稱": forms.Select(attrs={"class": "form-select"}),
            "路面狀況_路面狀態名稱": forms.Select(attrs={"class": "form-select"}),
            "路面狀況_路面缺陷名稱": forms.Select(attrs={"class": "form-select"}),
            "道路障礙_障礙物名稱": forms.Select(attrs={"class": "form-select"}),
            "道路障礙_視距品質名稱": forms.Select(attrs={"class": "form-select"}),
            "道路障礙_視距名稱" :forms.Select(attrs={"class": "form-select"}),
        }



class CombinedForm(forms.Form):
    accident_form = AccidentRecordsForm(prefix='accident')
    party_form = PartyInfoForm(prefix='party')
    causeanalysis_form = CauseAnalysisForm(prefix='causeanalysis')
    trafficfacilities_form = TrafficFacilitiesForm(prefix='trafficfacilities')
    road_form = RoadConditionsForm(prefix='road')