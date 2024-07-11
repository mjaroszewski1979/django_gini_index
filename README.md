## Global Macro
### This is a Django application designed to offer a user-friendly and visually appealing interface that engages users with dynamic and interactive graphs. The application leverages HTMX for asynchronous HTTP requests and Bokeh for powerful data visualizations.

### Features:
* Pandas-Datareader: Accesses and reads data from sources like FRED API.
* WhiteNoise: Serves static files efficiently without external services.
* Threading Module: Improves performance with concurrent task execution.
* Template Inheritance: Streamlines UI development and maintenance.
* Environment Variables: Securely stores API keys and credentials.
* Page Object Pattern: Enhances Selenium testing efficiency and maintainability.
* Optimized Performance: Uses the setUp method ensuring fast and reliable tests.

### Installation

1. Clone the repository:
  ```bash
  git clone https://github.com/mjaroszewski1979/django_global_macro.git
  cd django_global_macro
  ```  
2. Create a virtual environment:
  ```bash
  python3 -m venv env
  source env/bin/activate
  ```  
3. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```  
4. Set up environment variables:
   Create a .env file and add your configurations:
  ```bash
  FRED_API_KEY=<your-api-key>
  ```  
5. Apply migrations and start the server:
  ```bash
  python manage.py migrate
  python manage.py runserver
  ```

### Usage
* Access the application: Open your browser and go to http://127.0.0.1:8000/.
* View Data Visualizations: Interactive graphs based on fetched data.

### Testing

1. Run unit tests:
  ```bash
  python manage.py test
  ```  
2. Run Selenium tests:
  ```bash
  coverage run -p manage.py test tests_selenium
  ```  

### Code Coverage
* Selenium and unit tests combined

```bash
coverage run -p manage.py test htmx && coverage run -p manage.py test tests_selenium && coverage combine && coverage html

```

<img src="https://github.com/mjaroszewski1979/django_global_macro/blob/main/cov_report.png">

### Docker
#### Using Docker Compose

1. Clone the repository:
  ```bash
  git clone https://github.com/mjaroszewski1979/django_global_macro.git
  cd django_global_macro
  ```
2. Set up environment variables:
   Create a .env file and add your configurations:
  ```bash
  FRED_API_KEY=<your-api-key>
  ```  
3. Build and start the container:
  ```bash
  docker-compose up --build
  ```  

### Technologies Used
* Django: Web framework.
* HTMX: Asynchronous UI updates.
* Bokeh: Data visualizations.
* Pandas-Datareader: Data fetching.
* Docker: Containerization.
* HTML5UP!: Responsive and visually appealing HTML templates.
* Selenium: Automated browser testing to ensure application functionality.

### Contributing
* Fork the repository.
* Create a new branch (git checkout -b feature-branch).
* Make your changes and commit them (git commit -m 'Add new feature').
* Push to the branch (git push origin feature-branch).
* Open a pull request.

### Contact
For questions or feedback, please contact [mjaroszewski1979.](https://github.com/mjaroszewski1979)

![caption](https://github.com/mjaroszewski1979/django_global_macro/blob/main/gm_mockup.png)
  
 Code | Docker | Technologies
 ---- | ------ | ------------
[<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/github_g.png">](https://github.com/mjaroszewski1979/django_global_macro) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/docker_compose.png">](https://github.com/mjaroszewski1979/django_global_macro/blob/main/docker-compose.yml) | <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/python_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/django_g.png">  &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/htmx.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/bokeh.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/html_g.png"> <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/css_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/htmlup.png"> &nbsp; &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/js1.png"> &nbsp; &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/selenium.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/coverage.png">
