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

## CH08 SQLAlchemy 
Works with mySQL, SQLite, Postgres etc.
V powerful and adaptable
It's a full featured SQL abstraction
Mature and fast
A nice ORM we'll use in the course
Works on a unit of work basis
Can do eager loading to do one big query, rather than lots of little ones

### Architecture
Python can talk to many databases using a standard API
SQLALchemy builds on this with schema/types, a query language and an engine.
On top of this is an Object Relational Mapper (ORM) that you make with classes.

### The database model
PyCharm has some nice tools for modelling the database

Need to set up a connection to the DB
Need to model classes that map Python classes to tables
Need a base class to wire all this together 
When creating the class, the datatype comes from sqlalchemy
Can set the tablename sepeately to class name, As tables tend to be plural, class names are singular
__repr__ is a way to return useful info from the class while dedugging

### model base classes
In seperate file to avoid ciruclar dependencies. 
generated at runtime
can have multiple base classes

### connecting to the DB
Centereted around the unit of work. This is managed by a session
need to load the database. global init function does this only if db not already loaded
here you specify the kind o fdb you will use, in the create engine function
if echo is set to True, you'll get all the sql feedback. Good for debug
factory that creates the work units is bound to the engine

### creating tables
let sqlalchemy do it for us 
do this with metadata.createall. sqlalchemy needs to know about the tables though, so impor them first
pycharm will tell you it's unusused, progress though
once created, open db tab on RHS of Pycharm and drag the db across to it
Pycharm probably doesn' thave the correct driver, click the setings icon in db tab to find it 
in settings click "test connection" to check all is well
Double click on database name in the db tab to open a concole for sql queries
A file __all models__ is used to keep track of all the database classes you make, so they are imported when needed. You'll need to import them here
right click on the db and select diagrams, get a neat relational image of yoru db!

### indexes
optimise! a column with an index can be 10000 times faster on search query than one without, so put index=True on any var you may qurey to get all instances of across a table
Each of the columns you make in the db can have default values, required, indexes and more
NOTE: you pass the function, not the executed function, for e.g. datetime.now so it will be executed when queried, not when the app starts
sqlite will not edit tables once they are created. This prevents db loss, but prevents making prod changes to db. To update stuff, you have to drop the table or delete the db file

### Rest of the tables
BigInteger for ints
mainteners is interesting many to many mapping with both user_id and package_id as primary keys
We should set up some key relationships here? not covered in vid 
Import all these new dbs in all models.py in alphabetical order

### Relationships
in packages we make a relationship to releases so "releases" maps to the ids of the releases table. We do this with orm.relation. This is simple enough by itself, you normally want it ordered however, here's where order_by is handy. Can easily do order_by =  Relase.created_date.desc(). Or can make an ordered list of hierarchical orderings, as doen in the example.
This is good cos the database does the sort, this is v fast on an indexed column. Using back_populate links the info of the class you're editing to the entries it gets related to 
THe other class has to have an id column that exactly matches, except in name, linked with a foreignkey
protip: always remember to refresh your DB view in pycharm

### key concepts
All based on the sqlalchemybase class, noe per database
each of these classes has some attributes like name, email, version no
they can also have relationships
autoincrementing ids, default values are both neato
primary keys automatically have indices. Other things you'll sort on should have indices, they slow write time, but this is not a biggie
enforcing uniquensess can be handy (email address per user)

## CH10 using sqlalchemy

bin folder for admin tasks, not directly related to running the website
we need to init the db before anythign else

To create a new pacakge, we create a class instatnce then start a session to insert it into the db
you can use the relations set up betwen dbs to mean that you only need to explicitly add one, the other connected ones will be added too
creating data is neat! Just treat them like objects

### unit of work

this allows you to do lots of stuff before deciding to edit the db or not
You create each one with a session by calling session_factory() then sending it with a commit. Up to the commit there is no change to the db

### querying data home page
group numbers into nice comma seperate with "{:,}".format(number)
use simple queries in python files in the services folders to get aggreagte data on the db, e.g. totals

Should try to avoid accessing db from template, v resource wasteful. If you close the session, you can get detached errors. To avoid this, make sure all the access happens in the functions that are aggregating the data
the tool fro this is sqlalchemy.orm.joinedload
You can find out if you're making lots of db queries by running the app with engine echo=True
an engine ROLLBACK means to commit has been made, common after a query

Tip: when running on a new machine, make sure to create the database before trying to run the app

### Working with package details

Note the use of .strip().lower() to partially sanitise user input
Returning the .first() from a db query and having an Optional return also reduces chance of a crash

joined load stops data from leaking so you can close the session without crashing flask. This is probably the key part of the lesson. It's a little extra overhead, but usually worth it to fetch the linked releases to each package at time of query

### concept: querying data

Always starts by creating a session to start a unit of work
then do a query on that session followed by one or more filter statements to get just the data you need, followed by one to get just one record back, if wanted. Under the hood, this is doing a SELECT * from <TABLE> where <COLUMN> == x

If we want a set of items back, use .all() rather than .one()

Have a whole bunch of other filters like SQL, there is an ORM syntax for not equal, in, like etc.

### Concept ordering

dbs v good at filtering and ordering. Append .order_by() to your session.query, within the descriptor do .desc or .asc

### Concept updates
In order to update existing data, retrieve a record from the db, then update a record on that object:

package.author = "jack"

then to save it, call to session.commit() to do **all** changes

### Concept: relationships

Let us imagine connections in a standard Python program, rather than siloed like a db. To do this, we create an orm.relationship. You use back_populate to make sure it works both ways. In the other db, you specify a foreign key to get symmetry. All changes made to these dbs will be bidirectional too after a commit

### Concept: inserting data

session = session_factory()
package = Package()
package_id = 'sql'
package.author = 'mike'

release1 = Release()
release1.package = package
...

release2...

session.add(package)
session.commit()

All the above are now added to the db because of the relationships

## CH11 DB migrations with alembic

It's hard to change DBs when using an ORM. One of the bi challenges of dbs, one of the reasons for n-db solutions. However there is tooling available

If you try to add a field, can get a sqlalchemy operational error when the schema of the db do not match your query

Have to keep the db exactly in sync with the code. Two ways:

- Make a script to update the db when you change the production. Not hard in sqlite (just a file). Real problem is with seperate dbs where they get changed in development
- Use alembic. Created by the guy behind sqlalchemy.

Alembic is a db migration tool that tracks production and staging dbs. Alembic can patch your dbs. Doens't solve everything, but does solve a lot

### Getting started with Alembic

Add alembic to dev environment
run initla alembic command to init: alembit init alembic, in parent folder of app
You'll be told to edit an ini file
You have to add the sqlalchemy url path, this is the relative path to the db file
As you make changes to the db, they are stored as scripts in alembic/versions

pycharm note: if the db shows "no schema" or similar, make sure you right click on it >> properties >> test connection

There should be a table in the db `alembic_version` just above downloads. This should be a single row when working properly

The preferred way to make changes to the db is with alembic from the command line, not inserting in the app!

this looks very similar to git:

alembic revision --autogenerate -m "did a thing"

If you try this dry, will fail with metadata object error in alembic/env.py you need to update the `target_metadata` variable

after specifying the sqlalchemy base class (and all other sql classes you use) you need to coddle alembic by explicitly giving it a python path

When you run the autogenerate again, alembic makes a python file in alembic/versions. This contains commands to upgrade and downgrade. Does not change the db! Just makes a file to help you.

To change: alembic upgrade head

This will run the upgrades it needs to. Note the `alembic_version` table of the db to see where it's at

### More alembic changes
if you create a new class in your python files, then run the app, sqlalchemy will create it, not alembic

n.b when adding a new table, it has to be imported in `__all_models` or alebmic will not see it

alembic appears to just be a series of text files. as long as you didn't upgrade, you can just delete files it makes with no instructison in them (just pass) withoug issue

alembiuc helpers gives you functions that ask questions before editing the db. The example one will look at tables, and not create a new one only if column does not exist. If it tries to create a col that already exist, db will crash! this adds fault tolerences

### concept: getting started

pip install alembic
alembic init alembic
set connection string in alembic.ini at sqlalchemy.url
Note that if you used a relative path here, you'll have to run alembic from the right place!
Point to your sqlalchemy models in env.py
scripy.py.make generates the stuff to change the db
versions folders contains all the alembic changes like git

### concept: making a change

The reason to use autogen is that manual changes is a pain. You can do this by running a command line arguments from alembic to make a sekelton alembi cchange file, you then add the changes you want manually.  
It is safest to use a helper, as shown in final folder. To import it is a little weird, has to be done in each alembic version script. This is maybe just in the video?

Check what version you're on with `alembic current` or just check the version in the db
Upgrade with `alembic upgrade head`

### concept: auto-generating changes

Best way to run alembic is to let sqlalchmy pre-build the changes, then you can edit them. This is why we made the changes to env.py to point at the classes, then did autogenerate
Note that nothing happens when you autogenerate, only when you upgrade

## CH12 user submissions and html forms

Basics of an html form. Has an action and a method, action can be empty, meaning that url you submit it to is the same as the page you are on. http verb you want (method) is POST. You want this bc it is treated special, will not be cached and will warn you if you try to resubmit.

Then have input elements, e.g. of type test and type password. These can have an optional value that shows in the text box. They have names that you'll get out on the server side.

Have an error message that's shown if there is an issue, techinically outside of the form though

### GET-POST redirect pattern

1. User does a GET on the register page (after clicking register link)
2. We send them a form
3. They edit it locally
4. Theyt click submit that sends a POST to the server
5. Server does some validation
6. Server saves this data to the db
7. Send them a 302 redirect to get them to the welcome. This way, they don't get a warning on refresh

On wikipedia this is called post/redirect/get. Mike doesn't like it though as the order sounds wrong

### Register for site 

Need to register the blueprint for account views

Remember each view has a folder in templates

Note the use of GET and POST for the login and register functions in views/account. This is a much better design pattern than having a single login function with an if statement switch for GET vs POST. It's ok for these to have the smae namge as they have differing methods


### Registration form




