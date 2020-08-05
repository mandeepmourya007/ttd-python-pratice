from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView
from .models import Link


class LinkCreate(CreateView):
    model = Link
    fields = ["url"]