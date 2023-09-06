from ckeditor.fields import RichTextField

from django.db import models
from django.shortcuts import reverse

from core.models import TimeStamp
from topics.models import Topic
# Create your models here.


class Exercise(TimeStamp):

    title = models.CharField(max_length=200, verbose_name="موضوع")
    instruction = RichTextField(verbose_name="راهنما", blank=True)
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, verbose_name="مبحث")
    URL = models.CharField(max_length=200)

    class Meta:
        ordering = ("created", "updated")
        verbose_name = "تمرین"
        verbose_name_plural = "تمارین"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('exercise:exercise', args=[str(self.uuid)])


class ExerciseTip(models.Model):

    exercise = models.ForeignKey(Exercise, models.CASCADE, related_name="tips")
    tip = models.TextField()

    class Meta:
        ordering = ("exercise",)
        verbose_name = "راهنمایی"
        verbose_name_plural = "راهنمایی ها"

    def __str__(self):
        return self.tip
