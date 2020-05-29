from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields': ['q_text']}),
        ('Data Information',    {'fields': ['publish_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('q_text', 'publish_date')
    list_filter = ['publish_date']
    search_fields = ['q_text']


admin.site.register(Question, QuestionAdmin)
# The template of admin is located in django/contrib/admin/templates/admin/
admin.AdminSite.site_header = 'Django Polls'
