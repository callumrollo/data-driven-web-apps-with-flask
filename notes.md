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
if you click the link Pycharm provides, CSS is a mess. I don't know why. Just type it directly in browser

## CH05 Jinja templates
Python style logic with some particular syntax.
Renders to HTML as you would expect
Loops are written via {% for %} blocks. As are if. Correspongiding endif.
 {{}} to convert to text
 use href for links
Remember to mark your project home directory (one containgin app.py, templates etc) as sources root. THis way pycharm will do all kinds of autocompletion
Autocmpletion of html in jinja templates:
- span.title TAB expands to make a class called title within a span
You can call Python functions on the stuff in jinja templates. e.g. like upper() for strings

to get jinja autocompletion in PyCharm: file >> settings >> languages and frameworks >> template languages >> drop down list "jinja2"

### Bootstrap
this is pulled into the app via one line in header and 3 script lines down the bottom

### CSS
padding done for main here
make sure to use semi colons

### creating a common layout page
use a layout template with {% block %} to make holes for content. Content pages just contain the html to fill those holes
The baselayout file is for common stuff like HTML header, css, nav. Has several blocks for optional additions
blocks are optional! So can put in several with little cost
A content file that uses a layout starts with the key extend line, followed by however many optional blocks
If only one of these pages will use a particular resourse (like angluar JS) put that in the content file, not the base layout file. The blocks can contain imports as well as content

### response for a better render template

Some complex shit in infrastructure 
Function has some logic on what to do if your view returns a dict or a response when calling a template
This seems a bit overkill, but with more complicated views that may have many return lines, this makes for cleaner code 
So your functions in the main app just need to return data, not render templates

## Ch06 Routing and URLs

Important to have clean well organised urls. Think of them as a command line interface to your page, Also important for SEO (yuck)
Routing maps a url from a browser, to a view defined by your flask app logic. e.g. /about or packages/mysql
Flask will pass arguments from the url as varibales into your function

### Blueprints

We put these in views

Mostly they help by keeping bloat and detail out of app.py

views/package_views contains first intereseting stuff. This will generate a page for an url that specifies any package name

Views (Python) mirrors templates (jinja html) in layout and content

When creating a blueprint, you can make it active only on certain inputs (e.g. integers) by making the route int:<varname>

Routing lets you make different fucntions for different html methods. e.g. one function for GET and another for POST so you can serve a form to users and recieve their input data. The route is the same, but method kwarg of blueprint.route is specified

### Make a CMS
super quick and easy. Quite neat that this can be included in a data driven app.

To return a 404 page: flask.abort(404)

Use type path in route to pass a full url path to the function

After building this system that reads from a db, just need a simple system so users can enter details in markdown 

## CH07 frontend frameworks CSS and bootstrap

Bootstrap probs most popular frontend. So lots of demos and themes
Semantic UI is also v popular. Empahsises clean
Foundation is popular for professional designers. Bit more effort required
materialise

