## Global Macro
### This is a Django application powered by HTMX to assist in building rich client-side experience. It provides with access to highly interactive graphs created using Bokeh for more impactful data visualization. Users have now the opportunity to study clear, elegant, and insightful charts. Proper visualization brings clarity of data which helps in decision-making.

--------------------------------------------------

### Features:
* Connecting to FRED API using pandas-datareader as well as requests library to ensure the highest quality when importing historical time series
* Using threading module which allows a program to run multiple operations concurrently in the same process space
* Working with template inheritance mechanism to build a base “skeleton” template that contains all the common elements and defines blocks that child templates can override
* Taking full advantage of HTMX - dependency-free library to access modern browser features directly from HTML, rather than using javascript
* Serving static files with WhiteNoise to accomplish high performance and efficiency without depending on nginx, Amazon S3 or any other external service
* Implementing Bokeh's customizable parameters to gain full control over data visualizations when creating line charts, bar plots or hexagonal tiles to show binned aggregations
* Breaking logic into smaller parts by adding various new Django applications to an existing project 
* Storing app’s secure credentials in environment variables
* Utilizing setUp method to handle especially expensive setup operations for all of the tests within a module
* Performing extensive selenium tests using 'page object pattern' instead of making raw WebDriver calls to have cleaner code:
  * Utilizing DRY (Don’t repeat yourself) principle to minimize code duplication by having all ID-locators in one place
  * Setting an interface between web page’s elements and tests
  * Avoiding usage of WebDriver APIs in test methods
  * Encapsulating the services of web pages, not only exposing their elements

--------------------------------------------------

### Code Coverage:
* Selenium and unit tests combined

```
coverage run -p manage.py test htmx && coverage run -p manage.py test tests_selenium && coverage combine && coverage html

```

<img src="https://github.com/mjaroszewski1979/django_global_macro/blob/main/cov_report.png">

------------------------------------------------

![caption](https://github.com/mjaroszewski1979/django_global_macro/blob/main/gm_mockup.png)
  
  Live | Code | Docker | Technologies
  ---- | ---- | ------ | ------------
  [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/heroku_g.png">](https://quantcatalog.herokuapp.com) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/github_g.png">](https://github.com/mjaroszewski1979/django_global_macro) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/docker_compose.png">](https://github.com/mjaroszewski1979/django_global_macro/blob/main/docker-compose.yml) | <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/python_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/django_g.png">  &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/htmx.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/bokeh.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/html_g.png"> <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/css_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/htmlup.png"> &nbsp; &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/js1.png"> &nbsp; &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/selenium.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/coverage.png">
