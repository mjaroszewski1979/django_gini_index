import math
import pandas as pd
import pandas_datareader.data as pdr
import datetime
from django.shortcuts import render
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.embed import components
from bokeh.plotting import figure

years = range(2010,2019)
default_year = 2008
def get_data(symbols, start, end):
    result = None
    for symbol in symbols:
        df = pdr.DataReader(symbol['symbol'], 'fred', start, end)
        df = df.rename(columns={df.columns[0]: symbol['title']})
        if result is None:
            result = df.copy()
        else:
            result = pd.merge_asof(left=result.copy(), right=df, on='DATE')
           
    result = result.set_index('DATE')
    return result
symbols = [
    {'symbol': 'SIPOVGINIFRA', 'title': 'FRANCE'},
    {'symbol': 'SIPOVGINIITA', 'title': 'ITALY'},
    {'symbol': 'SIPOVGININOR', 'title': 'NORWAY'},
    {'symbol': 'SIPOVGINIPOL', 'title': 'POLAND'},
    {'symbol': 'SIPOVGINISWE', 'title': 'SWEDEN'},
    {'symbol': 'SIPOVGINIGBR', 'title': 'UK'},
]    


def index(request):
    year = request.GET.get('year', default_year)
    fred_data = get_data(symbols, start=year, end=year)
    data = {}
    for x in fred_data:
        data[x] = fred_data[x][0]
    a = sorted(data.items(), key=lambda x: x[1])
    countries = []
    vals = []
    for x in a:
        countries.append(x[0])
        vals.append(x[1])
    cds = ColumnDataSource(data=dict(countries=countries, vals=vals))
    fig = figure(x_range=countries, sizing_mode='stretch_both', title=f"GINI Index for ({year})")
    fig.title.align = 'center'
    fig.title.text_font_size = '1.5em'
    fig.xaxis.major_label_orientation = math.pi / 4
    fig.vbar(source=cds, x='countries', top='vals', width=0.8 )
    tooltips = [
        ('Country', '@countries'),
        ('GINI', '@vals')
    ]
    fig.add_tools(HoverTool(tooltips=tooltips))
    script, div = components(fig)
    context = {
        'script': script,
        'div': div,
        'years': years
    }
    if request.htmx:
        return render(request, 'partials/chart.html', context)

    return render(request, 'generic.html', context)

def home(request):
    return render(request, 'home.html')

'''def generic(request):
    return render(request, 'generic.html')'''



