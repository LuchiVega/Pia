from django.contrib import admin
from .models import Choice, Question

class ChoiceInline(admin.TabularInline): # Cambiado de StackedInline a TabularInline al final de la sección
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"] # Añadido en la sección de personalizar lista
    list_filter = ["pub_date"] # Añadido en la sección de personalizar lista
    search_fields = ["question_text"] # Añadido en la sección de personalizar lista

admin.site.register(Question, QuestionAdmin)