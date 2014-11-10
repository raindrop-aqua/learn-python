from django.db import models
from django.utils import timezone


class Question(models.Model):
    subject = models.CharField(max_length=200)
    description = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.subject

    def published_today(self):
        return self.publication_date.date() == timezone.now().date()

    published_today.boolean = True
    published_today.short_description = 'Asked today?'


class Answer(models.Model):
    question = models.ForeignKey(Question)
    content = models.TextField()
    best_answer = models.BooleanField("preferred answer", default=False)

    def __unicode__(self):
        return self.content
