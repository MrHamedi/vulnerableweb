from django.db import models
from ckeditor.fields import RichTextField
import uuid
from django.shortcuts import reverse
import os
# Create your models here.

def topic_image_upload_path(instance, filename):
    # Generate a unique filename using UUID and creation date
    topic_uuid = uuid.uuid4()
    ext = filename.split('.')[-1]
    filename = f'{topic_uuid}.{ext}'
    
    # Return the full file path
    return os.path.join('topic_images', filename)


class Topic(models.Model):

    uuid=models.UUIDField(primary_key=True ,default=uuid.uuid4 ,editable=False)
    title=models.CharField(max_length=200 ,verbose_name="موضوع" )
    text=RichTextField(verbose_name="متن")
    created=models.DateTimeField(auto_now_add=True ,verbose_name="تاریخ ایجاد")
    updated=models.DateTimeField(auto_now=True ,verbose_name="آخرین بروزرسانی")
    pic=models.ImageField(verbose_name="تصویر" , 
                          upload_to=topic_image_upload_path,
                          null=True
                          )

    class Meta:
        ordering=("created" ,"updated")
        verbose_name="مبحث"
        verbose_name_plural="مباحث"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('topics:topic_detail' ,args=[str(self.uuid)])