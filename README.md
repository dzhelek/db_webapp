# *db_webapp*
*CRUD web application with relational database*

## The task
The repository is solution to [this task](https://docs.google.com/document/d/1RwLIjDxtLztUuqs1XqzqZ5scpyIcyMoG86g41yRRZng/edit).

## Used technologies
* [Django](https://www.djangoproject.com/) - *The web framework for perfectionists with deadlines.*

## Database schema
![database schema](index.png)

## Tested on
* [Chrome 83 on Windows 10](https://www.google.com/chrome/?brand=CHBD&gclid=CjwKCAjwxqX4BRBhEiwAYtJX7Z5TXVXmvj_Zr9rl-3i7AvASqs3-qXbChik-lWxmuE--4HhvM_dYfRoCsYwQAvD_BwE&gclsrc=aw.ds)
* [Firefox 78 on Windows 10](https://www.mozilla.org/en-US/firefox/78.0/releasenotes/)

## How to test it
1. assert [python3.6](https://www.python.org/) or higher is installed
1. download the repository
1. `cd db_webapp`
1. `pip install -r requirements.txt`
1. `cd webapp`
1. `python manage.py migrate`
1. `python manage.py runserver`
1. open `localhost:8000/` in the browser 

