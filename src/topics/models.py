from django.db import models
from ckeditor.fields import RichTextField
import uuid
from django.shortcuts import reverse
# Create your models here.


class Topic(models.Model):

    slug=models.UUIDField(primary_key=True ,default=uuid.uuid4 ,editable=False)
    title=models.CharField(max_length=200 ,verbose_name="موضوع" )
    text=RichTextField(verbose_name="متن")
    created=models.DateTimeField(auto_now_add=True ,verbose_name="تاریخ ایجاد")
    updated=models.DateTimeField(auto_now=True ,verbose_name="آخرین بروزرسانی")

    class Meta:
        ordering=("created" ,"updated")
        verbose_name="مبحث"
        verbose_name_plural="مباحث"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('topics:topic_detail' ,args=[str(self.uuid)])