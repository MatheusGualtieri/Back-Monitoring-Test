from django.db import models


class AvgGraphInfo(models.Model):
    time = models.TimeField()
    status = models.CharField(max_length=50)
    total_count = models.IntegerField()
    avg = models.FloatField()

    avg_graph = models.ForeignKey(
        "avg_graphs.AvgGraph", on_delete=models.CASCADE, related_name="avg_graph"
    )
