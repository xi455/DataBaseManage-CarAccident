from django.urls import path

from transport import views

app_name = "transport"
urlpatterns = [
    path("", views.indexTemplateView.as_view(), name="index"),
    path("list/", views.CarAccidentListView.as_view(), name="list"),
    path("create/", views.CarAccidentCreateView.as_view(), name="create"),
    path("list/update/<int:pk>/", views.CarAccidentUpdateView.as_view(), name="update"),
    path("list/delete/<int:pk>/", views.CarAccidentDeleteView.as_view(), name="delete"),
]