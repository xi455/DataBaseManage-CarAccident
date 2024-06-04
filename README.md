# DataBaseManage-CarAccident System

## Introduction
This system is mainly for the database management of classroom final assignments, in addition to the functions of the database can be the basic operation of the addition of Chartjs chart function.

## Manipulation
```
python3.12 -m venv env && source env/bin/activate
```

## Data Import Execution
This command is for reading imported csv file, you can adjust the csv file name of the command file according to your needs.
```
python manage.py makemigrations && python manage.py migrate && python manage.py import_transport_subsidiary && python manage.py import_transport
```