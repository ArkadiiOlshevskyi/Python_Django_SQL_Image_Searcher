# Python_Django_SQL_Image_Searcher

Project Description:
 Python_Django_SQL_Image_Searcher is a small Python project that demonstrates how to work with a database query and images in Django and display them in a web browser. 
 It allows users to search for items and view them in a visually appealing manner with a parallax effect, similar to Pinterest. 
 The project uses Python 3.11, Django, PostgreSQL, and JavaScript to create an interactive and seamless user experience.

Installation:

  Install Python 3.11: Download and install Python 3.11 from the official Python website.
  Clone the repository: Use Git to clone the PyImageSearchParallax repository to your local machine.
  Install project dependencies: Navigate to the project directory and run pip install -r requirements.txt to install the required Python packages.
  Set up the PostgreSQL database: Install PostgreSQL, create a new database, and configure the database settings in django.py.
  Prepare the dataset: Create a folder to store the image dataset, ensuring it contains the relevant item images in JPG format.
  Run the migration: Execute python manage.py migrate to apply the database schema to the PostgreSQL database.
  Populate the database: Use sqlquery.py to insert the item information into the PostgreSQL database.
  Run the project: Execute python main.py to start the Django development server.
  Access the web page: Open your web browser and go to http://localhost:8000 to access the PyImageSearchParallax page.
  Search and view items: In the search bar, type the desired item (e.g., "fruits") to see the corresponding item tiles with a parallax effect.

Project structure:
  Python_Django_SQL_Image_Searcher/
  ├── main.py
  ├── django.py
  ├── sqlquery.py
  ├── README.md
  ├── requirements.txt
  ├── static/
  │   ├── css/
  │   │   └── style.css
  │   └── js/
  │       └── script.js
  ├── templates/
  │   └── index.html
  ├── dataset/
  │   └── (item images in JPG format)
  └── Python_Django_SQL_Image_Searcher/
      ├── __init__.py
      ├── settings.py
      ├── urls.py
      └── views.py
