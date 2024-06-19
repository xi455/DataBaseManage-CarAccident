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