# The tech stack we will use

using sqlalchemy with sqlite for data backend
Will also convert to mongodb
Bootstrap to make the front end  pretty

# What you can build with Python

- The Onion
- Spotify
- Pinterest
- PyPI
- bitbucket
- reddit is Python and sqlalchemy
- youtube

# CH2 Requirements
Python 3.6 minimum

# CH3 intro to Flask

Flask is a microframework. Flask doesn't provide databases etc. At the other end, building block frameworks like Django makes a whole webapp for your with a copmlex database/forum etc. Very simple to make but opinionated so restricts your options. Makes it a lot quicker

Bottle is even more minimalist, Pyramid a bit more opinionated. 

## Building blocks of Flask

Routes: URL patterns to views
View methods (aka controllers): main logic of the app. Takes inbound request and does the processing
MVC framework model view controller
Templates (aka views): Dunamic html will loop over model data and make nice html
Models: data passed to the view. Ofen kwargs or dictionaries
Static content: rich support for cached assets. V important for development, not so much for prod
Configuration: Dev, test, prod config. So our database/level of logging may change

### Views (MVC controllers)

Pass values to a template and render it
You can do logic like check if a user exists, if not create one

### Routes
Route is a url pattern stuff in < > will take a vriable
Can specify an html verb like POST
Static files will automatically eb served

### Models

Does some logic to collect data then passes it to a template. e.g. most popular packages. Data passed as kwargs. Can include data and methods

### Templates
Like HTML with some Python sprinkled in


## Ch04 first Flask app

### CLI setting up teh virtual environment

python -m venv venv 
./venv/bin/activate
pip install -U pip setuptools
pip install flask 

You'll have folders:
site
tests
venv

Make a requirements file

### Using Pycharm

start a project as Flask
Can select debug mode and other stuff by dropdown menu in upper right
run development server to run app locally

## Jinja templates
Python style logic with some particular syntax.
Renders to HTML as you would expect
Loops are written via {% for %} blocks. As are if. Correspongiding endif.
 {{}} to convert to text
 use href for links
Remember to mark your project home directory (one containgin app.py, templates etc) as sources root. THis way pycharm will do all kinds of autocompletion
Autocmpletion of html in jinja templates:
- span.title TAB expands to make a class called title within a span
You can call Python functions on the stuff in jinja templates. e.g. like upper() for strings


