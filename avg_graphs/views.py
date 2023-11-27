from django.forms import model_to_dict
from rest_framework import generics
from avg_graph_info.models import AvgGraphInfo
from .models import AvgGraph
from .serializers import AvgGraphSerializer
from avg_graph_info.serializers import AvgGraphInfoSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from transactions.permissions import IsSuperuserOrReadOnly


class GraphView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuserOrReadOnly]
    queryset = AvgGraph.objects.all()
    serializer_class = AvgGraphSerializer

    def perform_create(self, serializer):
        avg_graph_info = self.request.data.pop("avg_graph")
        serializer_graph = AvgGraphSerializer(data=self.request.data)
        serializer_graph.is_valid()
        created_graph = AvgGraph.objects.create(**serializer_graph.validated_data)
        serialized = AvgGraphInfoSerializer(data=avg_graph_info, many=True)

        graph_info = {f"{indice}": [] for indice in range(0, 24)}
        if serialized.is_valid():
            return serialized.save(avg_graph=created_graph)


class GraphDetailedView(generics.RetrieveDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuserOrReadOnly]
    queryset = AvgGraph.objects.all()
    serializer_class = AvgGraphSerializer
