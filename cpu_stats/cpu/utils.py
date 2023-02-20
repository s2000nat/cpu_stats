import datetime as dt


from django.conf import settings


from .models import Stats


def avg_count(x):
    """Функция вычисляет среднюю нашрузку за минуту """
    if len(x) > (60 // settings.TIME_PERIOD):
        x1 = x[-(60 // settings.TIME_PERIOD):]
        result = sum(x1) / len(x1)
        return round(result, 2)
    result = sum(x) / len(x)
    return round(result, 2)


def delete_old_stats():
    """Функция удаляет записи в БД старше 1 часа."""
    period = dt.timedelta(hours=settings.TIME_SLICE)
    time_lim = dt.datetime.utcnow() - period
    return Stats.objects.filter(measure_time__lt=time_lim).delete()

def continue_after_pause(close_socket_time):
    """Добавляет пустые промежутки времени, для которых нет данных"""
    if Stats.objects.all().count() != 0:
        now = dt.datetime.utcnow()
        delta = now - close_socket_time
        divider = dt.timedelta(seconds=settings.TIME_PERIOD)
        amount = delta // divider
        return Stats.objects.bulk_create(
            [Stats(cpu_load=0, avg_load=0) for i in range(amount)])








