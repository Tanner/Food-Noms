This is the README for Food Noms. Edit me. Fear me. Eat me.

## Required Packages
* [django-registration](https://bitbucket.org/ubernostrum/django-registration/)
* [django-profiles](https://bitbucket.org/ubernostrum/django-profiles/overview)
* [south](http://south.aeracode.org/)

## Installing food noms
To install food noms, you must perform the required steps.

0. Install [Python](http://www.python.org/) and [Django](https://www.djangoproject.com/).
1. Install the required packages above on your system.
2. You must now sync South up with the initial migration for **each** app.
>`python manage.py migrate [application_name] 0001 --fake`
3. You are done. Go home. Have a cookie.

## Using South
When you modify a applications model, instead of running:
>`python manage.py syncdb`

run:

>`python manage.py schemamigration [application_name] --auto`
     
That statement will create a migration file for the new model.

You must then apply this migration. You can do this with the command that the previous command outputs. It should look something like this:
>`python manage.py migrate [migratation_name]`

For more info on how to use South, take a look at the [documentation](http://south.aeracode.org/docs/index.html).
