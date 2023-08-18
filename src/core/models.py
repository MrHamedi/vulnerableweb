from django.db import models

# Create your models here.

class TimeStamp(models.Model):
    """
        A base Model with creation and update 
        time to get inherited by other models 
    """
    created=models.DateTimeField(auto_now_add=True ,verbose_name="تاریخ ایجاد")
    updated=models.DateTimeField(auto_now=True ,verbose_name="آخرین بروزرسانی")

    class Meta:
        abstract = True 
