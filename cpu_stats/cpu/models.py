from django.db import models


# Create your models here.
class Stats(models.Model):
    cpu_load = models.FloatField()
    avg_load = models.FloatField()
    graph = models.ImageField(
        'График',
        upload_to='graphs/%Y/%m/%d/%H/%M/',
        blank=True
    )
    measure_time = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ["-measure_time"]
