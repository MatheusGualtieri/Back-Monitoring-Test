from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from .views import (
    CustomTokenObtainPairView,
    UserDetailView,
    UserView,
)

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/<int:pk>/", UserDetailView.as_view()),
    path("users/login/", CustomTokenObtainPairView.as_view()),
    path("refresh/", jwt_views.TokenRefreshView.as_view()),
]
