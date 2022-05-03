from django.shortcuts import render
from .utilities import GiniIndex


def index(request):
    
    year = request.GET.get('year', 2008)
    gi = GiniIndex(year=year)
    context = gi.get_context()
    if request.htmx:
        return render(request, 'partials/chart.html', context)

    return render(request, 'generic.html', context)

def home(request):
    return render(request, 'home.html')

'''def generic(request):
    return render(request, 'generic.html')'''



