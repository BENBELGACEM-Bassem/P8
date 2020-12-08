README P8:

# Scope

This is the 8th project developed for Openclassrooms.
This django web application will let you find search for a substitute for a product of your choice. This substitute will be similar and with better nutrition score in order to help you adopt a healthier lfe style.
If you're logged in, you can save products and create your favorite list.

Can't wait to see what it looks like ?
Just visit this link ! https://bbgpurbeurre.herokuapp.com/

# Need to clone this project ?

A setting is mandatory to take advantage of this code: 
- Make sure python3 is installed
- Install a dependency manager if you choose to work in a virtual environment. For example, I used pipenv.
- Create a virtual environment and install dependencies (pipen install will install pipfile packages)
- On your postgres server, create a database named "purbeurre_db". Currently, User is set to 'admin' and password is set to 'p8', in the settings.py file, but you can change this and create your own credentials.

# Get the data

First, create tables by running django migration commands
Note that this application is sourced from Open Food facts API, and to load data, you need to run this command:
python manage.py fill_in_db [How much data you want]. 
By default, data will be loaded for 5 categories of products and 160 products per category.

# Test the code

Run the following command on the terminal, on project root directory:
coverage run --source='.' manage.py test
Then get a report by running:
coverage html
It will generate a htmlcov directory in the project's root. Launch index.html in your browser to see the results.









