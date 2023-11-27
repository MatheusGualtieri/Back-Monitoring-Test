import math
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import TransactionSerializer, SendEmailSerializer
from .models import Transaction
from .permissions import IsSuperuserOrReadOnly
from rest_framework.views import Response
from avg_graphs.views import GraphView
from avg_graph_info.models import AvgGraphInfo
from avg_graphs.models import AvgGraph
from avg_graphs.serializers import AvgGraphSerializer
from avg_graph_info.serializers import AvgGraphInfoSerializer
from datetime import datetime
from .services import MonitoringSystem
from rest_framework.response import Response
from rest_framework import status


class TransactionView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, many=isinstance(request.data, list)
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        serializer_graph = AvgGraphSerializer(
            data={"start": datetime.now(), "finish": datetime.now()}
        )
        serializer_graph.is_valid()
        created_graph = AvgGraph.objects.create(**serializer_graph.validated_data)

        graph = MonitoringSystem.generate_graph_info(data=self.request.data)
        for key, value in graph.items():
            for item in value:
                serializer_graph_info = AvgGraphInfoSerializer(
                    data={
                        "time": f"{key}:0",
                        "status": item,
                        "avg": value[item],
                        "total_count": math.ceil(value[item] * 60),
                    }
                )
                serializer_graph_info.is_valid(raise_exception=True)
                created_graph_info = AvgGraphInfo.objects.create(
                    **serializer_graph_info.validated_data, avg_graph=created_graph
                )
        MonitoringSystem.check_anomalies(self.request.data, self.request.user.email)
        return Response(graph, status=status.HTTP_201_CREATED, headers=headers)


class TransactionDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuserOrReadOnly]

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
