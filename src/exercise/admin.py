from django.contrib import admin
from .models import Exercise, ExerciseTip

class ExerciseTipInline(admin.TabularInline):
    model = ExerciseTip

class ExerciseAdmin(admin.ModelAdmin):
    ordering = ['created', 'updated']
    search_fields = ["topic", "title"]
    list_display = ["title", "topic", 'created', 'updated']
    inlines = [
        ExerciseTipInline
    ]

admin.site.register(Exercise, ExerciseAdmin)
