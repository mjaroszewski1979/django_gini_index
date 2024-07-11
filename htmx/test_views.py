# Import TestCase and Client for testing Django views
from django.test import TestCase, Client
# Import reverse and resolve for URL resolution
from django.urls import reverse, resolve

# Import views from the current module
from . import views


class GlobalMacroTest(TestCase):
    """
    Test case for testing the views of the Global Macro Django application.
    """

    def setUp(self):
        """
        Set up test fixtures before each test method.
        """

        # Create an instance of the Django test client
        self.client = Client()

    def test_home_url_is_resolved(self):
        """
        Test if the home URL is resolved correctly.
        """
        
        url = reverse('htmx:home')
        # Verify that the URL resolves to the correct view function
        self.assertEquals(resolve(url).func, views.home)

    def test_home_get(self):
        """
        Test the GET request to the home view.
        """
        
        response = self.client.get(reverse('htmx:home'))
        # Verify that the response contains the expected content and status code
        self.assertContains(response, 'Global Macro | Home', status_code=200)
        # Verify that the correct template is used in the response
        self.assertTemplateUsed(response, 'home.html')

    def test_gini_url_is_resolved(self):
        """
        Test if the Gini URL is resolved correctly.
        """
        
        url = reverse('htmx:gini')
        # Verify that the URL resolves to the correct view function
        self.assertEquals(resolve(url).func, views.gini)

    def test_gini_get(self):
        """
        Test the GET request to the Gini view.
        """
        
        response = self.client.get(reverse('htmx:gini'))
        # Verify that the response contains the expected content and status code
        self.assertContains(response, 'Global Macro | Gini Index', status_code=200)
        # Verify that the correct template is used in the response
        self.assertTemplateUsed(response, 'gini.html')
        # Verify that the partial chart template is used in the response
        self.assertTemplateUsed(response, 'partials/chart.html')
        # Verify that the script component is not None in the response context
        self.assertIsNotNone(response.context['script'])
        # Verify that the div component is not None in the response context
        self.assertIsNotNone(response.context['div'])
        # Verify that the years component is not None in the response context
        self.assertIsNotNone(response.context['years'])

    def test_cpi_url_is_resolved(self):
        """
        Test if the CPI URL is resolved correctly.
        """
        
        url = reverse('htmx:cpi')
        # Verify that the URL resolves to the correct view function
        self.assertEquals(resolve(url).func, views.cpi)

    def test_cpi_get(self):
        """
        Test the GET request to the CPI view.
        """
        
        response = self.client.get(reverse('htmx:cpi'))
        # Verify that the response contains the expected content and status code
        self.assertContains(response, 'Global Macro | CPI Index', status_code=200)
        # Verify that the correct template is used in the response
        self.assertTemplateUsed(response, 'cpi.html')
        # Verify that the partial chart template is used in the response
        self.assertTemplateUsed(response, 'partials/chart.html')
        # Verify that the script component is not None in the response context
        self.assertIsNotNone(response.context['script'])
        # Verify that the div component is not None in the response context
        self.assertIsNotNone(response.context['div'])
        # Verify that the inputs component is not None in the response context
        self.assertIsNotNone(response.context['inputs'])

    def test_stock_url_is_resolved(self):
        """
        Test if the stock URL is resolved correctly.
        """
        
        url = reverse('htmx:stock')
        # Verify that the URL resolves to the correct view function
        self.assertEquals(resolve(url).func, views.stock)

    def test_stock_get(self):
        """
        Test the GET request to the stock view.
        """
        
        response = self.client.get(reverse('htmx:stock'))
        # Verify that the response contains the expected content and status code
        self.assertContains(response, 'Global Macro | Stock Index', status_code=200)
        # Verify that the correct template is used in the response
        self.assertTemplateUsed(response, 'stock.html')
        # Verify that the partial chart template is used in the response
        self.assertTemplateUsed(response, 'partials/chart.html')
        # Verify that the script component is not None in the response context
        self.assertIsNotNone(response.context['script'])
        # Verify that the div component is not None in the response context
        self.assertIsNotNone(response.context['div'])
        # Verify that the inputs component is not None in the response context
        self.assertIsNotNone(response.context['inputs'])

    def test_handler404(self):
        """
        Test the 404 error handler.
        """
        
        response = self.client.get('/some_url/')
        # Verify that the response contains the expected content and status code for 404 error
        self.assertContains(response, 'Global Macro | Page not found', status_code=404)
        # Verify that the correct template is used in the response for 404 error
        self.assertTemplateUsed(response, '404.html')

    




