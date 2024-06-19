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
    
class CarAccidentUpdateView(GroupPerms, LoginRequiredMixin, UpdateView):
    model = AccidentRecords
    form_class = CombinedForm
    template_name = "caraccident_update.html"
    success_url = reverse_lazy('transport:list')  # Redirect to the list view upon successful update

    def form_valid(self, form):
        accident_record = form.save(commit=False)
        
        # Handle related objects if needed (similar to your create view)

        # For example, updating related objects if form has separate fields for them
        # party_info = get_object_or_404(PartyInfo, accident=accident_record)
        # party_info.field_name = form.cleaned_data['field_name']
        # party_info.save()

        # Save changes to AccidentRecords model
        accident_record.save()

        messages.success(self.request, "Car accident record updated successfully.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # You can add additional context data here if needed
        return context

    def get_object(self, queryset=None):
        # Get the instance of AccidentRecords based on URL parameter (pk)
        pk = self.kwargs.get('pk')
        return get_object_or_404(AccidentRecords, pk=pk)

    def get_initial(self):
        # Pre-fill form with initial data if needed
        initial = super().get_initial()
        # Example: initial data from related models
        accident_record = self.get_object()
        # initial['field_name'] = accident_record.related_field_name
        return initial
    
# class CarAccidentDeleteView(GroupPerms, generic.DeleteView):
#     model = AccidentRecords
#     template_name = 'caraccident_confirm_delete.html'
#     success_url = reverse_lazy('transport:list')

#     def get_object(self, queryset=None):
#         # 根據 URL 參數（pk）獲取 AccidentRecords 的實例
#         pk = self.kwargs.get('pk')
#         return get_object_or_404(AccidentRecords, pk=pk)

#     def get(self, request, *args, **kwargs):
#         # 覆寫 get 方法以添加刪除確認步驟
#         self.object = self.get_object()
#         return render(request, self.template_name, {'object': self.object})

#     def post(self, request, *args, **kwargs):
#         # 覆寫 post 方法以處理刪除確認
#         self.object = self.get_object()
#         success_url = self.success_url

#         self.object.delete()
#         messages.success(request, 'Car accident record deleted successfully.')
#         return redirect(success_url)
    
class CarAccidentDeleteView(DeleteView):
    model = AccidentRecords
    template_name = 'caraccident_confirm_delete.html'
    success_url = reverse_lazy('transport:list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(request, 'Car accident record deleted successfully.')
        return redirect(success_url)
