# image-repository
Image repo built with Django

This is an image repository dedicated to our furry friends! It is going to be a public web application that will make an attempt to only collect photos of our dogs or cats.
Guests must register an account with the application in order to post any images, and images must be accompanied with various data regarding information about the image.

This application was built with Django. It is a database with a little bootstrap magic to make it look nice. 

INSTRUCTIONS:
The application is still in development. In order to test the application, it must be done from a python friendly terminal using poetry
Python version 3.9 is required.

1.) clone the repository
2.) on the command line enter the following:
    poetry install
    poetry shell
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
5.) the development server will run on your local machine, and you can access the web app from the local server.
6.) Play around and enjoy!
