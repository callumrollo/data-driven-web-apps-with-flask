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
ctrl F5 in firefox to force refresh so things update 

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

### Bootstrap basics
Option 1: link to a CDN. No good for offline development though. Also external depenency
Option 2: npn install it. Keeps it simple

The basic is to link in the header to a CSS file from bootstrap. This is the CDN method.

Working on web stuff is hard bc browsers are inconsistent

If you don't explicitly set a style, the browser will do it. This can screw stuff up
Reset CSS combats this by explicitly setting everything, resolving many of these issues. THis is included in bootstrap

Grid layout is smart. Will compress three column apeareance into one on phones, or on shrinking, shuffles buttons. This is all part of bootstrap responsive layout. It's a bootstrap thing.
In firefox: web developer >> responsive design mode, you can test how the site looks on various devices

### Adding a grid
top level is a div container
then a bunch of div rows
each of these has columns
12 cols per line
Can break them up to e.g. 3 cols of width 4
md means medium: wrap when you get to medium size stuff. small will hang on to its grid a little longer as you shrink your browser window these have specific pixel size defs you can find
`div.container>div.row>div.col-md-4*3` then tab will aoutocomplete in pycharm

### Buttons and forms
some more html and CSS. Uses button class to apply bootstrap stlying
`    <button type="submit" class="btn btn-primary">Login</button>`
This class can also be applied to hyperlinks

### Syling the login
all done in the style section at top of body. V simple
You can set things to align and center automatically. Use padding to push stuff around if not quite right
bootstrap is "mobile first" so stuff can look real bad in wide screen unless contrained with e.g. max-width
clicking the color icon in the gutter in pycharm lets you pick a color
bootstrap class form-control applied to input boxes with have them fill out pleasingly
links as buttons look super nice. have siz button types and a plain link option

### Themes

Major benefit of bootstrap. so many themes! Loadsa free sites for this
startbootstrap.com for free themes
creative looks very nice
stylish-portfolio also good. BoldQ
unplash.com is great for free photos and graphics
sb-admin good for a dashboard
simple-sidebar is nice
also has a site for paid ones here. Cost around 20-30 dollars

## CH07 Site design

front page big text known as "hero section"
using more tab complete functionality in the one

### stats-slice
Can access CSS subparts with a space e.g. .maincontent h1 for h1 headers in maincontent
if it is a div in a div preface the term with a . e.g. main .main-item

### Nav bar header
bootstrap nav is very finicky and non-obvious
just copy an example from the botstrap website!
Fancy stuff in navbar makes it collapse and expand. Soem stuff added to make this work. Has an icon
some more CSS at the end to make the expanding nav bar work

### footer
use an html footer tag for this
make your footer background color the body background, then make main background white, this way get no black space under the header

