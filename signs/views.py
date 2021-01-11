from django.shortcuts import render
from .models import Dictionary
# Create your views here.


def home(request):

    dests = Dictionary.objects.all()

    return render(request, "index.html", {'dests': dests})