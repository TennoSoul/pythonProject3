from django.contrib import admin
from .models import ToDoUser
from .models import Event


# Register your models here.

admin.site.register(ToDoUser)
admin.site.register(Event)

admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'manager', 'event_date',)
    list_display = ('event_date', 'name', )
    list_filter = ('event_date', 'name', )
    ordering = ('-event_date',)