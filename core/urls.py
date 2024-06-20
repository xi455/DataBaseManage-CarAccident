"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView, TemplateView


urlpatterns = [
    path("", RedirectView.as_view(url="transport/"), name="index"),
    path("admin/", admin.site.urls),
    path("403/", TemplateView.as_view(template_name="403_csrf.html"), name="403"),
    path("transport/", include("transport.urls", namespace="transport")),
    path("error-report/", include("report.urls", namespace="report")),
    path("accounts/", include("users.urls")),
    path("chart/", include("chart.urls",namespace="chart")),
]

urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT,
)
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)