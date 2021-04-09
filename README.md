# Software Developer Assessment Test

Build an app that handles the process of creating an order for a retailer company. In this repository you will find the backend.

## File Descriptions

* [manage.py](manage.py): Django's command-line utility for administrative tasks.

### File Descriptions /retailer: 

Django configuration.

* [settings.py](/retailer/retailer/settings.py): Django settings file contains all the configuration of your Django installation. This document explains how settings work and which settings are available.


* [urls.py](/retailer/retailer/urls.py): Retailer URL Configuration. The `urlpatterns` list routes URLs to views.

* [wsgi.py](/retailer/retailer/wsgi.py): WSGI is the application callable which the application server uses to communicate with your code.

### File Descriptions /api: 


* [admin.py](/retailer/api/admin.py): Register your models here handle models from Django admin

* [models.py](/retailer/api/models.py): The representation of the entities in python that are the tables created in the database is detailed.


* [serializer.py](/retailer/api/serializer.py): We will declare a serializer that we can use to serialize and deserialize the data that corresponds to the objects.


* [urls.py](/retailer/api/urls.py): To design URLs for an app, you create a Python module informally called a URLconf (URL configuration). This module is pure Python code and is a mapping between URL path expressions to Python functions (the views).

* [views.py](/retailer/api/views.py): custom endpoint design:

Model Users.

'GET' Get all users: http://127.0.0.1:8000/users/

'GET' Get a user by id: http://127.0.0.1:8000/users/<user_id>

'POST' Create a user: http://127.0.0.1:8000/users/

Model Orders.

'GET' Get all orders: http://127.0.0.1:8000/orders/

'GET' Get a order by id: http://127.0.0.1:8000/orders/<order_id>/

'GET' Get a order by ids: http://127.0.0.1:8000/orders/<order_id>,<order_id>,<order_id>/

'GET' Get a order by user id: http://127.0.0.1:8000/orders/user/<user_id>

'GET' Get a order by date start-date end: http://127.0.0.1:8000/orders/<"year-month-day-year-month-day">/

'GET' Get a order by shipping: http://127.0.0.1:8000/orders/shipping/?city=<city_name>&state=<state_name>&country=<country_name>

'GET' Get order by id more shipping details: http://127.0.0.1:8000/order/<order_id>/shipping/detail/'

'GET' Get order by id more payment details: http://127.0.0.1:8000/order/<order_id>/payment/detail/

Model Shippings:

'GET' shipping information: http://127.0.0.1:8000/shippings/

Model Payments:

'GET' payment information: http://127.0.0.1:8000/payments/
## License
MIT License