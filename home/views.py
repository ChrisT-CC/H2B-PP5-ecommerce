""" home app views """
from django.shortcuts import render


def index(request):
    """ home view, returns the index page """

    return render(request, 'home/index.html')
