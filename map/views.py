from django.views.generic import TemplateView
import folium
from folium.plugins import MarkerCluster
from transport.models import AccidentRecords
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

class AccidentMapView(TemplateView):
    template_name = "accident_map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Query distinct years from AccidentRecords
        available_years = AccidentRecords.objects.values_list('發生年度', flat=True).distinct()
        context['available_years'] = available_years

        selected_year = self.request.GET.get('year')

        fmap = folium.Map(location=[25.041858, 121.525618], zoom_start=10)
        marker_cluster = MarkerCluster().add_to(fmap)

        if selected_year:
            accident_records = AccidentRecords.objects.filter(發生年度=selected_year)

            for record in accident_records[:2000]:
                folium.Marker(
                    location=[record.緯度, record.經度],
                    popup=record.發生年度,
                    icon=folium.Icon(color="red")
                ).add_to(marker_cluster)

        context['map_html'] = fmap._repr_html_()

        return context

class AccidentMapJsonView(APIView):
    def get(self, request, format=None):
        selected_year = request.GET.get('year')

        fmap = folium.Map(location=[25.041858, 121.525618], zoom_start=10)
        marker_cluster = MarkerCluster().add_to(fmap)

        if selected_year:
            accident_records = AccidentRecords.objects.filter(發生年度=selected_year)

            for record in accident_records[:2000]:
                folium.Marker(
                    location=[record.緯度, record.經度],
                    popup=record.發生年度,
                    icon=folium.Icon(color="red")
                ).add_to(marker_cluster)

        map_html = fmap._repr_html_()

        return Response({'map_html': map_html})
