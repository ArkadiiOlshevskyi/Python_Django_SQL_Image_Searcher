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





WORK WITH DATABASE

  Create and use Mysql database from shell terminal (on windows11)

1) install Mysql (workbench and shell) from ORACLE website (follow the guide , set your root user and password)
2) launch Mysql Shell terminalwindow
3) \sql		- type this to switch language in terminal so sql language
4) \connect root@localhost -p		- you are connecting to your sql database on server (you can use another server not localhost)
5) enter your password


* always ues ; in the end of command
** you can use ENTER and , also to wright multiline [open\close (parenteces)] commands but dont forget to finish it with ;


When connected you can start to work with your database
6) SHOW DATABASES;		- shows all databases awaliable in this local database(server)
7) CREATE DATABASE _________;		- where afrer in __ you tepe name of you database in lowercase with_
8) USE _________;	- use your __database to works with


Here is example of multiline command (use enter) for talbe creation:
9) CREATE TABLE ________ (
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(50),
	
);

10) 
