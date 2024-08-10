from django.shortcuts import render
from django.views.generic import ListView
from .models import NewsModel

# Create your views here.


class NewListView(ListView):
    model = NewsModel
    template_name = 'index.html'


def newslist(request):
    news = NewsModel.objects.all().filter(title="Kursk oblastida yakson etilgan Rossiya kolonnasi videosi. Bu haqda nimalar ma’lum?")
    context = {
        'object_list': news
    }

    return render(request, 'index.html', context)

