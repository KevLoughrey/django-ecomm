from django.shortcuts import render
from .models import Media

# Create your views here.
def view_all_items(request):
    # This function will handle displaying all items
    items = Media.objects.all()  # Assuming Media is the model for items
    context = {
        'items': items
    }
    return render(request, 'item/all_items.html', context)