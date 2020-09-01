# Django_Google_Maps
Django REST API with GraphQL and Docker accessing a GeoLocation API from Google

# What was done building the project

To build this project, I:

* installed Django 3.0 on a new Python 3.7 environment
* started a new Django project called "DjangoGoogleMaps"
* craeted a new Django app inside this project called "customers"
* created a database using MySQL called "customers"
* created a Model on "models.py", from the Django app "customers", that defined the tables to store the data coming from the file "customers.csv"
* used the migrate command from Django to create the tables on the database
* created a Django management command called "uploadCustomerDataToDB.py" that uploads the "customers.csv" data to the database, while querying the API from Google about GEO Location (getting the Latitude and Longitude for each customer)
* created two Views on Views.py from "customers" Django app that are used as Endpoints on the RestFul API
* created to URLs to allocated these Views on urls.py file
* setup the Graphql interface to have access to the same information as these Endpoints, and created a RestFul Endpoint just for GraphQL
* migrate the code and the database to a Docker installation
* setup the Dockerfile and docker-compose.yml file to build the project with Docker

# About the files on the root folder

* The urls.py file contains the URLs path for the RestFul Endpoints. There are three paths there: "allCustomers/", "customerByID" and "graphql". When the server is running, all you need to do is to access them using a browser with the address like this "http://localhost:8000/"endpoint-name/".

    Example:

        * "http://localhost:8000/allCustomers/
        * http://localhost:8000/customerByID/"ID", where ID is the number ID of a specific customer
        * http://localhost:8000/graphql/

* The views.py filed inside the "customers" folder has two functions:  allCustomers and customerByID. The first one returns an HTTP Response as JSON with data from all customers. The second one returns an HTTP Response as JSON with data from only one especific customer, defined by the input ID given to the function.

* Inside the folder "customers\management\commands" there are two files: the customer.csv and the Django management command "uploadCustomerDataToDB.py".

# About GraphQL

To do queries on GraphQL you can write the commands "allCustomers" or "customerByID" on GraphQL interface.

# About the Django management command "uploadCustomerDataToDB.py"

This command has to functions. One is the getGEO, which receives as input the city name and state name, connects to Google API to query the Latitude and Longitude, and returns a dictionary with both information.
The other function is the "handle", which is the main function inside a Django command. It loads the "customers.csv" file (this works only inside the Docker container with Linux), loop over each customer on dataset, calls the function getGEO each time, and save the information inside MySQL database.

# About MySQL Server

The "settings.py" file inside "DjangoGoogleMaps" folder has the information about the database that Django should use. Now it is set to a database running inside the container after a Docker installation.

# How to run the project

To run the project you need a Windows machine with Docker 3 installed. Just go to the root folder and execute the command "build_everything.bat". It will run the commands "docker-compose build" e docker-compose up". After it finished loading the two virtual machines (one for Django and the other for MySQL Server), you can run "createdb.bat". This command will run the migration of database (creating the necessary tables), run the Django management command "uploadCustomerDataToDB.py", and restart the web container with Django installed. Once this is done, you can access the Endpoints on localhost:8000. You need to execute this two commands only once. After it is runnig, if you stop the machines, you just need to restart them.

# IMPORTANT INFORMATION

To run the final step with the command "uploadCustomerDataToDB.py", you need to define your Google API Key isn the docker-compose.yml file. Inside this file there is an environment variable called GOOGLE_API_KEY. You need to write your Google API Key there.


