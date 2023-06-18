# Food Delivery Service - Backend Server App

This project is a DRF API app created as part of Assignment 3 of FSE Web Development Course.

## Developers - Group4
- Umesh Kumar Sharma (Student Id: 2022CFSE006)
- Pallavi Sheshrao Mundwaik (Student Id: 2022CFSE034)
- Praveen R (Student Id: 2022CFSE019)

## Running the project

To run the project you need Node and npm installed. 

1. Download or clone from git Hub
2. Create a python virtal environment using virtualenvwrapper-win

    mkvirtualenv fdsenv  
    workon fdsenv
    
4. Install packages:
5. pip install django
6. pip install djangorestframework
7. pip install django-cors-headers
8. pip install psycopg2    
9. pip install -U drf-yasg
10. Run the backend server  

    python manage.py runserver
 
11. Ports   
  http://127.0.0.1:8000/  
  http://127.0.0.1:8000/admin/  
    
  Endpoints Get Trains  
  http://127.0.0.1:8000/fds/rest/api/trains  
  
  Swagger endpoint  
  http://127.0.0.1:8000/swagger/

## Test users

1. UID001 (Customer) - password: BITS2023$
2. RID001 (Restaurant) - password: BITS2023$
3. admin - password: BITS2023$

## One time tasks  
  python manage.py makemigrations  
  python manage.py migrate  
### End of File

