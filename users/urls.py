from django.urls import path, include

from users.views import UserListView, CustomUserCreateView, CustomPasswordChangeView, UserDeleteView

urlpatterns = [
    path("register/", CustomUserCreateView.as_view(), name="user_register"),
    path("password_changes123/", CustomPasswordChangeView.as_view(), name="custom_password_change"),
    
    path("list/", UserListView.as_view(), name="user_list"),
    
    path("detail/<pk>/", UserDeleteView.as_view(), name="user_detail"),
    path("delete/<pk>/", UserDeleteView.as_view(), name="user_delete"),
    
    path("", include("django.contrib.auth.urls")),
]