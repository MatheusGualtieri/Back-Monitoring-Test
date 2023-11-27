from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from .views import CustomTokenObtainPairView

urlpatterns = [
    path("users/", views.UserView.as_view()),
    path("users/<int:pk>/", views.UserDetailView.as_view()),
    path("users/login/", CustomTokenObtainPairView.as_view()),
    path("refresh/", jwt_views.TokenRefreshView.as_view()),
]