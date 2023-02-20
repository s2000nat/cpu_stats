from django.contrib import admin


from .models import Stats


class StatsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'cpu_load', 'avg_load', 'graph',)
    search_fields = ('cpu_load',)
    list_editable = ('cpu_load', 'avg_load',)
    empty_value_display = '-пусто-'


admin.site.register(Stats, StatsAdmin)
