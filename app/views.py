from django.shortcuts import render
from django.views.generic import ListView
from .models import NewsModel

# Create your views here.

class NewListView(ListView):
    model = NewsModel
    template_name = 'index.html'

