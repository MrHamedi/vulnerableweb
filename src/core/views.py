from django.shortcuts import render
from django.views.generic import ListView
from topics.models import Topic
# Create your views here.


class Homepage(ListView):
    model=Topic
    template_name="core/homepage.html"
    context_object_name="topics"