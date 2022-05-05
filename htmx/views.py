from django.shortcuts import render
from .utilities import GiniIndex, CpiIndex


def index(request):
    
    year = request.GET.get('year', 2008)
    gi = GiniIndex(year=year)
    context = gi.get_context()
    if request.htmx:
        return render(request, 'partials/chart.html', context)

    return render(request, 'generic.html', context)

def home(request):
    return render(request, 'home.html')

def cpi(request):

    symbol = request.GET.get('symbol', 'FPCPITOTLZGPOL')
    cpi = CpiIndex(symbol=symbol)
    context = cpi.get_cpi_context()
    if request.htmx:
        return render(request, 'partials/chart.html', context)

    return render(request, 'cpi.html', context)




