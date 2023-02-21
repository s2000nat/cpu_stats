from django.db import models


# Create your models here.
class Stats(models.Model):
    cpu_load = models.FloatField()
    avg_load = models.FloatField()
    measure_time = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ["-measure_time"]
