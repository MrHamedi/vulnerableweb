from django.urls import path 
from . import views

app_name="topics"

urlpatterns = [
    path("<uuid:pk>/" ,views.TopicDetailView.as_view() ,name="topic_detail")
]