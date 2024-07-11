# Import render function for rendering templates
from django.shortcuts import render
# Import GiniIndex, CpiIndex, and StockIndex classes from the utilities module
from .utilities import GiniIndex, CpiIndex, StockIndex

def home(request):
    """
    Handle the home page view.
    
    Args:
        request (HttpRequest): The HTTP request object.
    
    Returns:
        HttpResponse: The rendered home page.
    """
    
    return render(request, 'home.html')

def gini(request):
    """
    Handle the GINI index view.
    
    Args:
        request (HttpRequest): The HTTP request object.
    
    Returns:
        HttpResponse: The rendered GINI index page or partial chart.
    """

    # Get the year from the request, default to 2008 if not provided
    year = request.GET.get('year', 2008)
    # Create an instance of GiniIndex with the specified year
    gi = GiniIndex(year=year)
    # Get the context for the GINI index plot
    context = gi.get_context()
    
    if request.htmx:
        # Render a partial chart if request is an HTMX request
        return render(request, 'partials/chart.html', context)

    # Render the full GINI index page
    return render(request, 'gini.html', context)

def cpi(request):
    """
    Handle the CPI index view.
    
    Args:
        request (HttpRequest): The HTTP request object.
    
    Returns:
        HttpResponse: The rendered CPI index page or partial chart.
    """

    # Get the symbol from the request, default to 'FPCPITOTLZGPOL' if not provided
    symbol = request.GET.get('symbol', 'FPCPITOTLZGPOL')
    # Create an instance of CpiIndex with the specified symbol
    cpi = CpiIndex(symbol=symbol)
    # Get the context for the CPI index plot
    context = cpi.get_cpi_context()
    
    if request.htmx:
        # Render a partial chart if request is an HTMX request
        return render(request, 'partials/chart.html', context)

    # Render the full CPI index page
    return render(request, 'cpi.html', context)

def stock(request):
    """
    Handle the stock index view.
    
    Args:
        request (HttpRequest): The HTTP request object.
    
    Returns:
        HttpResponse: The rendered stock index page or partial chart.
    """

    # Get the stock symbol from the request, default to 'SP500' if not provided
    stock = request.GET.get('stock', 'SP500')
    # Create an instance of StockIndex with the specified stock symbol
    stock = StockIndex(stock=stock)
    # Get the context for the stock index plot
    context = stock.get_stock_context()
    
    if request.htmx:
        # Render a partial chart if request is an HTMX request
        return render(request, 'partials/chart.html', context)

    # Render the full stock index page
    return render(request, 'stock.html', context)

def page_not_found(response, exception):
    """
    Handle 404 page not found errors.
    
    Args:
        response (HttpResponse): The HTTP response object.
        exception (Exception): The exception that was raised.
    
    Returns:
        HttpResponse: The rendered 404 error page.
    """
    
    return render(response, '404.html')

def server_error(response):
    """
    Handle 500 server errors.
    
    Args:
        response (HttpResponse): The HTTP response object.
    
    Returns:
        HttpResponse: The rendered 500 error page.
    """
    
    return render(response, '500.html')





