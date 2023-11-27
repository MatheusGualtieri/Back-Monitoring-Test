from django.urls import path
from .views import GraphView, GraphDetailedView

urlpatterns = [
    path("graphs/", GraphView.as_view()),
    path("graphs/<int:pk>", GraphDetailedView.as_view()),
]
