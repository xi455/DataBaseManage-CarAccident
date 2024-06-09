from django.contrib import messages

from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.base import RedirectView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from report.models import ErrorReport
from report.forms import ErrorReportForm
from utils.perms import GroupPerms


def CheckRepair(request, pk):
    report = get_object_or_404(ErrorReport, pk=pk)
    report.處理狀態 = "已處理"
    report.save()
    
    messages.success(request, "已確認修復回報")
    return redirect("report:list")


def CheckOverrule(request, pk):
    report = get_object_or_404(ErrorReport, pk=pk)
    report.處理狀態 = "駁回"
    report.save()
    
    messages.success(request, "已確認駁回回報")
    return redirect("report:list")


class ErrorReportListView(GroupPerms, generic.ListView):
    model = ErrorReport
    template_name = "report_list.html"
    context_object_name = "reports"
    paginate_by = 20

    def get_queryset(self):
        return ErrorReport.objects.all().order_by("-回報日期")
    

class ErrorReportCreateView(LoginRequiredMixin, CreateView):
    model = ErrorReport
    form_class = ErrorReportForm
    template_name = "report_form.html"
    
    def form_valid(self, form):
        messages.success(self.request, "回報已成功送出")
        form.instance.用戶 = self.request.user

        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "回報送出失敗")
        return super().form_invalid(form)
    
    def get_success_url(self) -> str:
        if self.request.user.groups.filter(name="intendant").exists() or self.request.user.is_superuser:
            return reverse("report:list")
        
        return reverse("user_profile")
    

class ErrorReportDetailView(LoginRequiredMixin, generic.DetailView):
    model = ErrorReport
    template_name = "report_detail.html"
    context_object_name = "report"