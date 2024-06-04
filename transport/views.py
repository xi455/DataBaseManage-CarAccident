from django.contrib import messages

from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.base import RedirectView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from transport.models import (
        AccidentRecords,
        PartyInfo,
        CauseAnalysis,
        TrafficFacilities,
        RoadConditions,
    )
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
    

class CarAccidentListView(generic.ListView):
    model = AccidentRecords
    template_name = "caraccident_list.html"
    context_object_name = "caraccident_list"
    queryset = AccidentRecords.objects.all()[:50]
    order="-發生日期"

class AccidentRecordsCreateView(CreateView):
    model = AccidentRecords
    fields = "__all__"
    template_name = "accidentrecords_create.html"
    success_url = reverse_lazy("transport:list")