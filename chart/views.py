from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from django.db.models import Count,Prefetch
from rest_framework.views import APIView
from rest_framework.response import Response
from transport.models import AccidentRecords,RoadConditions,CauseAnalysis,PartyInfo
from django.db.models.functions import Substr
from rest_framework.request import Request
from django.db.models import IntegerField
from django.db.models.functions import Cast
from collections import defaultdict
User = get_user_model()

class HomeView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html')



def get_data(request, *args, **kwargs):
    data = {
    }
    return JsonResponse(data) # http response


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = {}
        qs = AccidentRecords.objects.annotate(month_as_int=Cast('發生月份', IntegerField())).values('發生月份').annotate(count=Count('發生月份')).order_by('month_as_int')
        labels = [entry['發生月份'] for entry in qs]
        default_items = [entry['count'] for entry in qs]
        
        qs1 = AccidentRecords.objects.values('發生年度').annotate(count=Count('發生年度')).order_by('發生年度')
        labels1 = [entry['發生年度'] for entry in qs1]
        default_items1 = [entry['count'] for entry in qs1]
        
        qs2 = AccidentRecords.objects.values('事故類別名稱').annotate(count=Count('事故類別名稱')).order_by('事故類別名稱')
        labels2 = [entry['事故類別名稱'] for entry in qs2]
        default_items2 = [entry['count'] for entry in qs2]
        
        qs3 = AccidentRecords.objects.annotate(short_location=Substr('發生地點', 1, 3)).values('short_location').annotate(count=Count('id')).order_by('-count')
        labels3= [entry['short_location'] for entry in qs3]
        default_items3 = [entry['count'] for entry in qs3]
        
        qs4 = AccidentRecords.objects.values('發生年度', '發生月份').annotate(count=Count('發生月份')).order_by('發生年度', '發生月份')
        result_dict = defaultdict(list)
        for item in qs4:
            year = item['發生年度']
            count = item['count']
            result_dict[year].append(count)
        result_dict = dict(result_dict)
        
        road_conditions_qs = RoadConditions.objects.only('道路型態大類別名稱')
        qs5 = (AccidentRecords.objects
            .annotate(short_location=Substr('發生地點', 1, 3))  # 提取發生地點的前三个字符
            .prefetch_related(Prefetch('roadconditions_set', queryset=road_conditions_qs))
            .values('short_location', 'roadconditions__道路型態大類別名稱')  # 反向引用 roadconditions
            .annotate(count=Count('id'))  # 统计每个分组的记录数量
            .order_by('-count'))  # 按数量降序排序        
        default_items5 = [[f"{entry['short_location']}: {entry['roadconditions__道路型態大類別名稱']} - {entry['count']}"] for entry in qs5]
        
        
        causeanalysis_qs = CauseAnalysis.objects.only('肇事逃逸類別名稱_是否肇逃')
        qs6 = (AccidentRecords.objects
            .prefetch_related(Prefetch('causeanalysis_set', queryset=causeanalysis_qs))
            .values('發生年度', 'causeanalysis__肇事逃逸類別名稱_是否肇逃')  # Reverse reference roadconditions
            .annotate(count=Count('id'))  # Count the number of records for each group
            .order_by('-count'))  # Order by count in descending order
        result_dict1 = defaultdict(lambda: defaultdict(int))
        for item in qs6:
            year = item['發生年度']
            hit_and_run_type = item['causeanalysis__肇事逃逸類別名稱_是否肇逃']
            count = item['count']
            result_dict1[year][hit_and_run_type] += count
        result_dict1 = {year: dict(hit_and_run_types) for year, hit_and_run_types in result_dict1.items()}
            
            
        qs7 = (AccidentRecords.objects
            .annotate(short_location=Substr('發生地點', 1, 3)) 
            .prefetch_related(Prefetch('causeanalysis_set', queryset=causeanalysis_qs))
            .values('short_location', 'causeanalysis__肇因研判子類別名稱_主要') 
            .annotate(count=Count('id')) 
            .order_by('-count'))  
        default_items7= [[f"{entry['short_location']}: {entry['causeanalysis__肇因研判子類別名稱_主要']} - {entry['count']}"] for entry in qs7]
        partyinfo_sq = PartyInfo.objects.only('保護裝備名稱')

        qs8 = (AccidentRecords.objects
        .values('事故類別名稱')
        .prefetch_related(Prefetch('partyinfo_set', queryset=partyinfo_sq))
        .values('事故類別名稱', 'partyinfo__保護裝備名稱')
        .annotate(count=Count('partyinfo__保護裝備名稱')) 
        .order_by('事故類別名稱', '-count'))

        default_items8 = [[f"{entry['事故類別名稱']}: {entry['partyinfo__保護裝備名稱']} - {entry['count']}"] for entry in qs8]
        data = {
            "labels1": labels1,
            "default1": default_items1,
            "labels": labels,
            "default": default_items,
            "labels2": labels2,
            "default2": default_items2,
            "labels3": labels3,
            "default3": default_items3,
            "default4": result_dict,
            "default6":result_dict1,
            "default5": default_items5,
            "default7": default_items7,  
            "default8": default_items8
            }
        
        return Response(data)

