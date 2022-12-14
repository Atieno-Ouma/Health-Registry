

# Introduction

Health Registry is a generic web based health registry.

### Main features

* Create an Entry(Client,Facility)
* View the list of entries
* Update the Entries
* Generate Report
* Delete Entries

 ![My Image](core/static/images/sc1.png)
 ![My Image](core/static/images/sc2.png)
 ![My Image](core/static/images/sc3.png)
* MySQL Database Used as the default Database Engine

# Usage

To set-up and get started with the project:



# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git https://github.com/Atieno-Ouma/Health-Registry.git
    $ cd Health-Registry
    
Activate the virtualenv for your project.

### Existing virtualenv


If your project is already in an existing python3 virtualenv first: 


    $ source venv/bin/activate
  
Install project dependencies:

    $ pip install -r requirements/local.txt
    
   ### No virtualenv

This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

If you don't have django installed for python 3 then run:

    $  pip install -r requirements.txt
    
And then configure the`settings.py` file with your database credentials for the project:

    DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your database',
        'USER': 'your user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
    




    
Then simply make  migrations:

    $ python manage.py makemigrations
    
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver


