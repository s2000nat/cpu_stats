import datetime as dt
import json
from psutil import cpu_percent
from time import sleep


from django.conf import settings
from channels.generic.websocket import WebsocketConsumer


from .models import Stats
from .utils import avg_count, delete_old_stats, continue_after_pause

stat_list = []
close_socket_time = dt.datetime.utcnow()


class WSConsumer(WebsocketConsumer):
    def connect(self):
        global close_socket_time
        self.accept()
        delete_old_stats()
        continue_after_pause(close_socket_time)
        for i in range(settings.TIME_OF_WORK // settings.TIME_PERIOD):
            delete_old_stats()
            cpu_stat_now = cpu_percent()
            stat_list.append(cpu_stat_now)
            Stats.objects.create(
                cpu_load=cpu_stat_now,
                avg_load=avg_count(stat_list),
            )
            y_avg = Stats.objects.values_list('avg_load', flat=True).order_by('id')
            y_cpu = Stats.objects.values_list('cpu_load', flat=True).order_by('id')
            self.send(json.dumps({'y1': list(y_avg),
                                  'y2': list(y_cpu)}))
            sleep(settings.TIME_PERIOD)
        self.close()

    def close(self, code=None):
        global close_socket_time
        close_socket_time = dt.datetime.utcnow()


