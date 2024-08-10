from django.urls import path
from .views import NewListView, newslist

urlpatterns = [
    path('news/', NewListView.as_view(), name='index'),
    path('', newslist, name='new_list')
]