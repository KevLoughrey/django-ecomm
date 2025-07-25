from django.urls import path
from .views import view_all_items

urlpatterns = [
    path('', view_all_items, name='view_all_items'),
]
