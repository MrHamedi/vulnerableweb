from django.urls import path 
from . import views

app_name="topics"

urlpatterns = [
    path("<uuid:pk>/" ,views.topic_detail ,name="topic_detail")
]