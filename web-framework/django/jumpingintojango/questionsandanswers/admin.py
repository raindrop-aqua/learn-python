from django.contrib import admin
from models import Question, Answer


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ['subject', 'publication_date', 'published_today']
    list_filter = ['publication_date']
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)

