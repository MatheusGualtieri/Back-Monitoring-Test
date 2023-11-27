from rest_framework import serializers
from .models import AvgGraph
from avg_graph_info.serializers import AvgGraphInfoSerializer


class AvgGraphSerializer(serializers.ModelSerializer):
    avg_graph = AvgGraphInfoSerializer(many=True)

    class Meta:
        model = AvgGraph
        fields = "__all__"
        depth = 1
