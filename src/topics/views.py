from django.shortcuts import render
from django.views.generic import DetailView
from topics.models import Topic
# Create your views here.


class TopicDetailView(DetailView):
    model=Topic
    template_name="topics/topic_detail.html"