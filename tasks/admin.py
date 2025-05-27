from django.contrib import admin
from .models import Category, Event, Participant

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_description')
    search_fields = ('name',)
    
    def get_description(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
    get_description.short_description = 'Description'

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time', 'location', 'category')
    list_filter = ('category', 'date')
    search_fields = ('name', 'location')

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
