from django.contrib import messages

from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.base import RedirectView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from transport.models import (
        AccidentRecords,
        PartyInfo,
        CauseAnalysis,
        TrafficFacilities,
        RoadConditions,
    )
from transport.forms import CombinedForm
from transport_subsidiary.models import UnitName, VehicleType

from utils.perms import GroupPerms

# Create your views here.


class indexTemplateView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["accident_records"] = AccidentRecords.objects.all()[:1000]
        context["party_info"] = PartyInfo.objects.all()
        context["cause_analysis"] = CauseAnalysis.objects.all()
        context["traffic_facilities"] = TrafficFacilities.objects.all()
        context["road_conditions"] = RoadConditions.objects.all()
        return context
    

class CarAccidentListView(GroupPerms, generic.ListView):
    model = AccidentRecords
    template_name = "caraccident_list.html"
    context_object_name = "caraccident_list"
    queryset = AccidentRecords.objects.all()[:50]
    order="-發生日期"


class CarAccidentCreateView(GroupPerms, generic.View):
    template_name = "caraccident_create.html"

    def get(self, request, *args, **kwargs):
        form = CombinedForm()

        context = {
            "form": form,
        }

        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = CombinedForm(request.POST)

        if form.is_valid():
            accident = {k[len("accident-"):]: v for k, v in form.data.items() if k.startswith('accident-')}
            accident["處理單位名稱警局層"] = get_object_or_404(UnitName, pk=accident["處理單位名稱警局層"])
            accident = AccidentRecords(**accident)
            accident.save()

            party = {k[len("party-"):]: v for k, v in form.data.items() if k.startswith('party-')}
            party["當事者區分_類別_大類別名稱_車種"] = get_object_or_404(VehicleType, pk=party["當事者區分_類別_大類別名稱_車種"])
            party["accident"] = accident
            party = PartyInfo(**party)

            causeanalysis = {k[len("causeanalysis-"):]: v for k, v in form.data.items() if k.startswith('causeanalysis-')}
            causeanalysis["accident"] = accident

            if causeanalysis["肇事逃逸類別名稱_是否肇逃"] == "unknown":
                causeanalysis["肇事逃逸類別名稱_是否肇逃"] = None
            
            elif causeanalysis["肇事逃逸類別名稱_是否肇逃"] == "true":
                causeanalysis["肇事逃逸類別名稱_是否肇逃"] = True

            else:
                causeanalysis["肇事逃逸類別名稱_是否肇逃"] = False

            causeanalysis = CauseAnalysis(**causeanalysis)

            trafficfacilities = {k[len("trafficfacilities-"):]: v for k, v in form.data.items() if k.startswith('trafficfacilities-')}
            trafficfacilities["accident"] = accident
            trafficfacilities = TrafficFacilities(**trafficfacilities)

            road = {k[len("road-"):]: v for k, v in form.data.items() if k.startswith('road-')}
            road["accident"] = accident
            road = RoadConditions(**road)

            party.save()
            causeanalysis.save()
            trafficfacilities.save()
            road.save()

            messages.success(request, "Car accident record created successfully.")
            return redirect('transport:list')
        
        context = {
            "form": form,
        }

        return render(request, self.template_name, context=context)
    

from transport.forms import AccidentRecordsForm, PartyInfoForm, CauseAnalysisForm, TrafficFacilitiesForm, RoadConditionsForm

class CarAccidentUpdateView(GroupPerms, generic.View):
    template_name = "caraccident_update.html"

    def get(self, request, *args, **kwargs):
        accident = AccidentRecords.objects.get(pk=kwargs["pk"])
        accident_form = AccidentRecordsForm(instance=accident)
        party_form = PartyInfoForm(instance=PartyInfo.objects.get(accident=accident))
        causeanalysis_form = CauseAnalysisForm(instance=CauseAnalysis.objects.get(accident=accident))
        trafficfacilities_form = TrafficFacilitiesForm(instance=TrafficFacilities.objects.get(accident=accident))
        road_form = RoadConditionsForm(instance=RoadConditions.objects.get(accident=accident))

        form = CombinedForm(
            accident_form=accident_form,
            party_form=party_form,
            causeanalysis_form=causeanalysis_form,
            trafficfacilities_form=trafficfacilities_form,
            road_form=road_form,
        )
        
        context = {
            "form": form,
        }

        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = CombinedForm(request.POST)

        if form.is_valid():
            accident = get_object_or_404(AccidentRecords, pk=kwargs["pk"])
            party = get_object_or_404(PartyInfo, accident=accident)
            causeanalysis = get_object_or_404(CauseAnalysis, accident=accident)
            trafficfacilities = get_object_or_404(TrafficFacilities, accident=accident)
            road = get_object_or_404(RoadConditions, accident=accident)

            # 分類數據        
            accident_data = {key: value for key, value in request.POST.items() if key.startswith('發生年度') or key.startswith('發生月份') or key.startswith('發生日期') or key.startswith('發生時間') or key.startswith('事故類別名稱') or key.startswith('處理單位名稱警局層') or key.startswith('發生地點') or key.startswith('天候名稱') or key.startswith('光線名稱') or key.startswith('經度') or key.startswith('緯度')}
            party_data = {key: value for key, value in request.POST.items() if key.startswith('當事者區分_類別_大類別名稱_車種') or key.startswith('當事者性別名稱') or key.startswith('當事者事故發生時年齡') or key.startswith('保護裝備名稱') or key.startswith('當事者行動狀態子類別名稱') or key.startswith('車輛撞擊部位子類別名稱_最初') or key.startswith('車輛撞擊部位大類別名稱_其他') or key.startswith('車輛撞擊部位子類別名稱_其他')}
            causeanalysis_data = {key: value for key, value in request.POST.items() if key.startswith('肇因研判大類別名稱_主要') or key.startswith('肇因研判子類別名稱_主要') or key.startswith('肇因研判子類別名稱_個別') or key.startswith('肇事逃逸類別名稱_是否肇逃')}
            trafficfacilities_data = {key: value for key, value in request.POST.items() if key.startswith('號誌_號誌種類名稱') or key.startswith('號誌_號誌動作名稱')}
            road_data = {key: value for key, value in request.POST.items() if key.startswith('道路型態大類別名稱') or key.startswith('道路型態子類別名稱') or key.startswith('事故位置大類別名稱') or key.startswith('路面狀況_路面鋪裝名稱') or key.startswith('路面狀況_路面狀態名稱') or key.startswith('路面狀況_路面缺陷名稱') or key.startswith('道路障礙_障礙物名稱') or key.startswith('道路障礙_視距品質名稱') or key.startswith('道路障礙_視距名稱')}
            
            accident_data["處理單位名稱警局層"] = get_object_or_404(UnitName, pk=accident_data["處理單位名稱警局層"])
            accident_form = AccidentRecordsForm(accident_data, instance=accident)
            accident_form.save()

            party_data["當事者區分_類別_大類別名稱_車種"] = get_object_or_404(VehicleType, pk=party_data["當事者區分_類別_大類別名稱_車種"])
            party_data["accident"] = accident
            causeanalysis_data["accident"] = accident
            trafficfacilities_data["accident"] = accident
            road_data["accident"] = accident

            
            party_form = PartyInfoForm(party_data, instance=party)
            party_form.save()

            causeanalysis_form = CauseAnalysisForm(causeanalysis_data, instance=causeanalysis)
            causeanalysis_form.save()
            
            trafficfacilities_form = TrafficFacilitiesForm(trafficfacilities_data, instance=trafficfacilities)
            trafficfacilities_form.save()

            road_form = RoadConditionsForm(road_data, instance=road)
            road_form.save()

            messages.success(request, "Car accident record created successfully.")
            return redirect('transport:list')
        
        context = {
            "form": form,
        }

        return render(request, self.template_name, context=context)
    


class CarAccidentDeleteView(GroupPerms, generic.View):
    def post(self, request, *args, **kwargs):
        accident = get_object_or_404(AccidentRecords, pk=kwargs["pk"])
        accident.delete()

        messages.success(request, "Car accident record deleted successfully.")
        return redirect('transport:list')