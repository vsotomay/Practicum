For this project it is recommended to use Python 3.4, which the latest version of Flask is compatible with.

The pip command uses the Python Packages Index to install new Python packages made by others. 
This makes it super-easy to install Flask and other packages that you might want to use in future.

The pip command may already be installed. Try running pip in the terminal. If that does not work, download most
recent version of pip, and install by running in the directory the download is stored in. 

$ python get-pip.py --user

This isn't necessary but virtualenv makes it easy to use different packages, 
and even different versions of packages, in your Python projects. This project already contains the "virtual environment" 
for this project in the /flaskenv directory, but on your machine you can set up virtualenv on your project and keep 
Flask and it’s dependencies contained to just that project by running.

$ pip install --user virtualenv

Create a Python 3 virtualenv under the 'flaskenv' directory

$ virtualenv --python=python3 flaskenv

Activate the virtual environment

$ source flaskenv/bin/activate

The last step, activate sets up your terminal/command prompt session for using a contained Python3 installation in the flask-workshop directory. 
If you start up a new terminal then you will need to repeat the activation step again. The deactivate command can be used to return your terminal back to normal.

Now that we are in our virtual environment, we can install Flask.

$ pip install Flask

The database dependency for this project is of MongoDB, so it is necessary to install that to the virtual environment as well.

$ pip install Flask-PyMongo

