# Readme

This repository contains a django project for making and tracking reservations.

### Setup
```
git clone https://github.com/hrezaeianzadeh/django-screen-listing.git

cd django-screen-listing

docker-compose build

docker-compose run django clean

docker-compose up
```

### API Endpoints
```
[POST]
/api/reservation
To make a reservation

[POST]
/api/check
To check available rooms at a certain time

[POST]
/api/overview
Sends back a response with overview of booked rooms for a listing. You must send a parameter with name `listing_name` to the endpoint.
```

### Running Tests
There are test cases implemented to:
1. Make a reservation
2. Check available rooms at a certain time

After running the containers with docker-compose you can execute bash into the django container with the command:
```
docker exec -it django-screen-listing_django_1 bash
```
and executing the command:
```
python3 manage.py test
```
to run the tests. The test codes are implemented in `base/tests.py` and you can look into them for more information on the parameters that should be sent to endpoints.
