from rest_framework import serializers
from .models import AvgGraphInfo


class AvgGraphInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvgGraphInfo
        fields = "__all__"
        read_only_fields = ["avg_graph"]
