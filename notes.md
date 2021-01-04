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

Prefer placeholder to label in fillable fields like registration email boxes

Over in `account_views` the /account/register GET function runs each time the site is visited, the corresponding POST function runs when the submit button is pushed

Do most of the styling in a custom css sheet in css. This is linked in the block "addition css" at the bottom of the register.html

Some styling of fields and buttons is by bootstrap (the class in the html)

To adjust suff within in a block (e.g. all fields in the form) use:
`form.account-form > * {CSS stuff}`

To stop stuff breaking out the bottom of forms:
`<div style="clear: both;"></div>`

### register POST action

the form submits the name and user entered value in each field as a key-value pair, so give each field a name

using a default empty string for email also doing lower and strip to make it cleaner


### Getting the submitted values 

We want to a) use the values and b) round trip the values i.e. stop them dissappearing if the user hits "submit" and there is an issue

We do this with an error catch in views that returns the dictionary of values and returning the value in register.html value="{{ name }}"

### Creating the user

Never store password directly in the database! instead, use passlib. This will hash and verify passwords. It will salt automatically and does multiple rounds of hashing

Also need to check if the user exists already before making another one. Ensure unique email for this

### Login forms

Start from a clone of the registration page
check if the email matches one in the db
Use verification from the passlib library to check the password against the hash

### Create a user session (cookie)

So that the site recognises the user logged in
These are fairly simple in Flask, combining it with the redirect and response is a littel trickier
Stopping the cookie being tampered with needs some thinking. Can't just make it a simple number!
Much of the logic in is infrastucutre/cookie auth. This is pretty well self described
Takes a user ID and hashes it up, then it makes a val based on this user id and the hash value. This is the cookie I think
You can set the cookie timeout

The authentication step is in `get_user_id...` this checks that it hasn't been tampered with. This is how we recover the user id

To check that the cookie has been created:
Login on site
Inspect element
Refresh page
Network >> HTML >> account >> Cookies

in the account index function, adding logic for cookies

If the user is not logged in (no cookie)  >> redirect to login page
If the user is matched, return it

Some important redirects here. 

### Nav based on users session

control this from shared layout. This won't work by itself though, as you have to pass `user_id` from every view!
fix the ugly way first

### Sources of data

Can come from the form, the url, from a query string... Not a great pattern!
Lets have just one place to ask about where stuff may have been passed
We do this by creating a unified merged dictionary
This is in `request_dict` of infrastructure. Works by taking arguments passed by flask with `**route_args` works from least (url strings) to greatest (additional args) priority
This creates a single RequestDictionary
This saves awkward r.get("value") style stuff, returns None if the requestedd value doesn't exist, avoiding awkward crashes
. It takes the flask.request by default
This allows things to look much nicer and cleaner, for instance in login get of account view. You no longer care where the data came from.

I guess this isn't essential if you are happy to keep track of where all your data are coming from

This is very much a Michael thing, not basic flask

## CH13 client and server side validation

### Motivation for view models

Last time we had very little checks and validation. These are essential
Will use a design pattern called viewmodels. This is not Flask native, but tused in lots of other web apps.
Presently we pass around user and user id. When it comes to something like post we have to roundtrip lots of data, an error message and user. This is not ideal. Also we need more checks! More granular checks on fields etc.
Viewmodels simplifies all this

### Viewmodel base class

Data exchange is deeply tied to html template and the view method that passes stuff to it. This will be the viewmodels job to do all the data exchange and validation. Each one is particualr to the template + view model combo, but they have common features. e.g. everyone has the user auth token check and an optional error.

We start this class with a flask request and the common reqiest dict we created in the previous chapter
It has optional error message and optional user id
We need this to return a dictionary of values (e.g. the email, name etc from register form)
This is a good base class, but to be useful we need specific views

### Using a viewmodel

First example is from the account index page. Note that the init takes no args bc no args are passed to this view. because of this you need super init? unsure
we can use `self.user_id` as the base class already set this up

Now, when calling this view model as vm, it does all the validation and field generation for us. We can just return the dict from vm. Even if it has some unused values in, that's fine

### The register viewmodel

Here we make use of the common `request_dict` to collect all the data together. As the fields 

Enahnced check: self.name.strip() checks for names made only of spaces. Also check for short passwords etc. All this is in the viewmodel

Back in the view, the only check you need is if there is an error in the validation

sqlalchemy: detatched instance error! Not in my session, but in Michael's. This happens when your db gets out of sync with the session after you make a change and commit a transaction

For this, we're doing some magic over in `data/db_session create_session` function. sqlalchemy is normally super safe, so makes sure that you can't mess with data you commited. Specifically stops you looking at values after they've been commited.  We are making that false here, so you can shove stuff at the db. We may not want this! 

This whole thing radically simpoifies data exchange and validation

### Viewmodel concept

User submits a form via an HTTP POST. Flask and many other web frameworks encourage a super complicated view method. All the validation, cleaning, checking in this viewmodel. Get a lot of duplication this way
The viewmodel pattern puts all that elsewhwere. This makes teh code cleaner and easier to test. View method is not more maintanable.

The value of this also makes shunting data around much easier. All you ever need do is return the vm.dict

### Viewmodel data exchange

Viewmodels provide data exchagne/normalistaion and data validation
The dictionary is core to this
Important to have default user id and error
The other derived viewmodels (concrete veiwmodels) just have to enter data in these fields that will be returned as a dict
The super init sets all this base stuff, then the concrete model adds more stuff to the dict.

### Concept: server side validation

These are all our checks for if the form is ok. This is usually the only time you have to validate. You can return friendlier errors with your validation fails if you wish. e.g. if a user already exists, do you wanna reset your password?

### Client side validation with HTML5

If you have a slow ping, validating on the server can be slow and annoying
By simply adding the key word argument required to the html, this will be validated client side, and will not submit until they are all filled
You can also use more sophisticated types like email for each form field
Can also do stuff like setting a min or max value for the fields
Client side validation will not protect you from malicious POSTs. Some stuff can't be done on user side like checking if an email is already registered

## CH14 testing web apps

Write tests to find bugs. Make CI with e.g. Travis meaningful.

Testing web apps have particular challenges. Tend to have more tangled dependencies. There are lots of implicit things needed, like a request, a reguest.form, cookie... Often needs a db to check against. How do you test a redirect? email?

Test frameworks have all we need

### Types of test

Note we're not covering basic unit tests here
3 groups: view models, view and integration.

View models are simplest, also important as they do the validation. They implicitly use request

Next, a view method wraps the view model. We test this next, it also uses request. Need to provide a controlled input

Full web app, including the db init. We can test this with stuff from flask as if the web app was running. Can simulate a browser

Can finally spin up a full test server and hit it with Selenium to get a user erquivalent test. Not covered in this course

### Organizing tests in flask

We want logical organisation for tests just like the app itself. TYpically, we group out tests in the same way
sitemap.xml lists all the links in your site. Mostly to help search engines
We can cover a bunch of cases by requestinge every page from the sitemap. What often happens is a super major fail that gives a 500 or a 404. Easy to catch at least

### Getting started with tests

We could use unit tests or pytest, however, in the flask doc all of them use pytest. So we'll use that

To run pytest in PyCharm: edit configurations, + python tests, pytest. Path to script to your pytest script

Tests will never be called by a human so you can make the names very descriptive

**3 As of testsing: Arrange, Act then Assert**

First challenge of testing form validation: how to get the form data into flask. We do it with a context manager. This stuff goes in test client and is talked about in the flask documentation.
This is the function `test_request_context` from the flask app that is used as a context manager, so we can pass form data to the viewmodel as if it came from a user
Next we have an issue that we cannot talk to the db! Don't want the db though, how do we get around this?

### Avoiding db calls on register

To do this, we can replace the function that normally calls the db with another one by using mock from unittest. Again, we put this in a context manager so it doesn't affect the rest of the test. 
Cool thing: Can also return "FOUND" as if from an sql query in the mock statement to test that functionality too

### Testing registration when inputs are invalid

We should write tests for all foreseeable cases, password missing, too short etc. In this bit of mocking, we set the returned email from the db to be the same as that submitted on the form

Set the string searches in your tests just specific enough, so they don't fall over if you slightly change the wording of your error messaged

### Testing veiw methods

We do two layers of mocking so that the test an existing user in not found in the db and a user is succesfully created. we teest that teh response has the correct location

There is a nice way to de-indent this, shown in the final folder

### Concept testing view methods

We can assume that validation and data exchange are fine. We need to test that the view method is using these responses correctly

If we test a simple page with no db, we import a method from views, create a context manager which is just a request to '/' then we capture the response. Methods always return a response. We test that the status code is 200 and that other things returned are as expected (e.g. list of packages is longer than 0)

For a more realistic version, we need a fairly complicated test to mock the db. We impor the project, import a Package class and create a fake test package with releases. We mock out the function that would look for a package by id and return our mock package, likewise for release. We set the context to project/sqlalchemy. We have to pass the package id directly to the function.

Finally, we test the returned package aginast our expected fake data.

### Integrated tests

Time to fire up flask and run full tests on the app
We will test the account page. Two scenarios: if user is logged in they see it. It user is not logged in they get redirected

We don't want to really run flask though. Here is where pytest fixture comes in, client over in `test_client`. When you pass it as a variable, it registers blueprints and sets up a db. Then it yields out a client. Note that you have to pass the test function the object `client`

The test for no user is simple, as no succesful check of the db is expected. To test for a user that is logged in will be a bit more tricky, we need to mock the db return, just as we did before. Note that this is bocking it from hitting the db, so the db is outside the scope of this test

Note that to search for a string in the output of this page, you need to look in the binary, so prepend the string with a b

### The rest of the tests

Split test by naming them by type e.g. `test_vm_...` for viewmodel tests
We dump all the tests into an `_all_tests` file so we can run them all in one
At the point, `test_int_site_mapped_urls` is failing. This may be intentional as I don't think I've made a sitemap yet? Should check

### Running tests outside of pycharm

activate the virtual env, run `pytest _all_tests.py --disable-warnings` it's not happy! Doesn't find `pypi_org` wouldn't be an issue if we packaged it up. Or we can add some boiler plate to the beggining of all tests to add stuff to the path. Pycharm does this for us.

### pareto principle and testing with sitemaps

The sitemap can be found at site home/sitemap.xml this is primarily for search engines and lists all the pages of the site. This can be big as it lists every page, may want to cache it

You can limit the number of items in your sitemap. All this stuff in in seo view. Have to list last updated time too. There's some unpleasant looking stuff in the sitemap template. This sets the base static files and loops through the packages

In the tests we let it hit the db, as we want to test with the real pacakges. We use Python xml stuff to find all the urls and a quick replace. On each one we do a client.get() to check if they exits. We only really need to test one. There's some complicated stuff. Need to do some text replacement on the xml text.

This is working in final but not in starter. Not certain why...

Sitemap testing is v important and easy tests.

possible check out https://buildstaticwebsites.com/guides/why-you-need-a-sitemap-and-how-to-create-one-with-flask

## CH15 Deployment

Using a standard linux server on the cloud. Will work on linude, azure, AWS etc.

Could use heroku to grab fro github: easier but more expensive

Won't cover setting up a db server. Advantage of sqlite it's just a file

- Get an Ubuntu server
- Install NGINX, this is what people talk to on port 80, does http and https
- NGINX serves up static files, it delegates running Python code to
- uWGI (micro whisgy) this will handle Python requests.
- Need to be aware of the GIL that inhibits parallelism within a single process
- Beneficial to multiprocess, we'll get uWGI to spin off lots of itselves. 
- So we'l have lots of sites in parallel

Topology:
Req comes in over https, hits NGINX, from here on, just http is fine, passes it to uWSGI, uWSGI decides which worker process will take it, this gets passes back through the layers to the client

### Creating a linux server
We'll use digital ocean, linode is very similar

Standard setup with Ubuntu LTS. So far identical to linode

### Setup script and config files

Need to setup uWSGI and nginx. This is performed with three scripts in the server directory next to `pypi_org` 

bash script has all the steps you'd apply to a server to get a good working state with all dependencices and firewalls. A few lines are interactive but most can be run all in one. Better to do bit by bit though.

The way we're running it doesn't make uWSGI happy, as you just imoport it from the app, rather than running it. This is covered by the else: configure in app main. uWSGI won't do this though, it won't do teh configure commadn for instance. This tweak is necessary to get uWSGI to play ball, there are other ways


The unitfile in pypi.service is for a background daemon. Runs when system starts. 

### Configure the server

We use git to get files to the server

Working through the bash file:

nload for monitoring traffic
tree for dir structure
use fail2ban to blacklist teh spammers
Next some port opens: 22 for ssh, 80 for requests, 443 for ssh
Then enable it. Double check you allowed 22!

github config to remember creds for a month

Setup a bunch of folders for the app, note that the base is 777
Haven't setup logging in this course, should do this

System is solely dedicated to this site, could just use the system Python. This is risky if we break it though, use a virtualenv as instructed here. Note activattion of venv. Can also use:
. venv/bin/activate

httpie is like curl or wget, lets us test out app, is nicer
glances in a gui that helps you understand whats running. Like htop
need uwsgi within the environment

### Make virtualenv always active
just pop source /apps/venv/bin/activate at the end of zshrc. Standard

### Setting up our code

With the app running in one terminal, open another on the server and do
http localhost:5006 
to see the http of the page 

### Running under uWSGI

uWSGI properly runs the python code in production. Controlled by pypi.service
Has options for the virtual environment, number of process and threads, http address. Best thing to test first is to run the command called Exec Start. This requires a python file wsgi.py at the top level directory

With this v basic file in place, running the exec comand from the correct directory will work. Check again with http, noting that it's probs on 5000 now
Check back on the runing uWSGI for response code and speed. Subsequent page requests will be quicker

### uWSGI as a service

back in the bash script, copy the daemon
service is now setup under the name pypi. Can be controlled with systemctl
Probs shouldn't be running as root tho :/
Hit it with the http to check
This is now running in background so you can logout. This will restart with the server too after reboots
We're not currently opening the 5000 port, so it won't show outside

### Running in nginx

This is all the user sees
If we visit the servers ip in a browser, we'll see nginx is up
We need it to run our code, back to the shell script
Remove the site enabled default nginx
Then copy over our pypi.nginx this includes:
listen on port 80 
server name (www.google.com or whatever) this way, the same nginx can serve lots of sites
don't pass back the server version (serer tokens)
location of static files, just handled by nginx. These are cahced for a year
otherwise try files over at 5000
Micael likes to use http internally, can use unix sockets. This is more performant, but http is easier to test
This site is online! Awesome

One thing I missed was loading in the data. Should have all been in starter, but somewhere we pointed toward final. Looks like it was in the pypi.service file

### Adding SSL with let's encrypt

We want a domain name and to secure with SSL
We need the fake servername in pypi.nginx or let's encrypt won't work? unsure
This gets a little confusing, read some more articlee
managed to get a free domain from noip.com just set the ip address there correctly
Success! Secured with lets encrypt. Only needs the commands form the bash file
When answering the SSL questions, yes to redirect

Need to setup a cron job or manually renew the certs every 90 days

### Concept uWSGI

We could have a lot more threads per process
Final forward slash in runtime dir is essential
Best to run exec command seperately first to check

### nginx concept
listen on 80
set the domain name in servername have to buy a real one to get SSL
Static gets our static content
/ tries against the application, we pass to uWGI through localhost

## CH16 MongoDB

The most popular document db
Why tho? no problems with migrations
NB not doing anythign in starter here, all in final

### how do doc dbs work

Very different to relational dbs. No tables. Much closer to the style of memory (hierarchichal). So you have nested stuff in them, like a precomputed join. These can have indexes added to the nested so speed of simple lookup is not lost

### Connecting to mongoDB

As with SQL, don't run the quiries directly, we have a higher engine, called teh mongoengine

check out setup in nosql/mongosetup

We have a dbname. We have a series of db aliases, you can have multiple dbs. THis is chosen in db connection
You need to specify quite a few things about secirity, users etc.

Consequentially, setting up the db over in app is a lot simpler

In practive, probs get usernmae and password from a file so doesn't get into git

because we put all our db access in a few files in services, it's easy to adap tto mongodb

### user entity with mongoengine

sqlalchemy and mogoengine have a lot of similarities
We're making all the equivalent stuff in the nosql folder to model off of the data folder
Compare the way that users.py is done in mongo vs sql in these two folders
Defalut behaviour is a little different. In mongo nullable is always true. Indexes a specified somewhere else.
We drop a couple of the fields bc we never used them in the app

### Saving a user
This is in `user_service/create_user` 
saving is simpler, no unit of work just user.save()
There are lots of wyas to look at mongodb. An app called robo3t makes it easy
When we view the documents, see that they are just like json
`_id` in the svaed file, but just .id when you access it from the system

Implicit behind this is that MongoDB is running on your PC

### The rest of the entities

It's all very similar to mysql, just semantics of setting it up
You can overwrite the primary key if you want
In packages you start to leverage the advantages of mongodb
No more need for maintaner id project id normalisation table for many to many relationship.
In mongodb ou just need a list of maintainer ids in each project to identify which users are associated with each project

### Rewriting our quiries

You can just write a query in the view method, shouldn't thoufh. instead, just need to rewrite the stuff in services which is nice. Hooray for design patterns. Cookie management is slightly complicated though
Way simpler to query a db in mongo. You jsut get an object and list it. Very Python. PAckage quer also simpler, no objects, no joins... no double =
With lots of small methods in one place, it's quick and easy to switch over to mongo

### Fixing the login

we get an error with object id, bc we are using cookies. However, mongodb reqiures a bson object (binary json I think?) whatever, easy fix.

### Importing data to mongodb

There's a cool techinique to migrate from any sqlalchmey db to mongodb
bin/migrate
You init both db connections, be caerful not to overwirte, so starts with a check for a clean db in mongo
we just loop through the stuff table by table, field by field
You can do bulk inserts with mongo engine if lots of data, not necessary here
Check imports for differential between the common class names
bwtter check all your data made it over

### home page cleanup
relationships can trip you up, if you set them before in sql
You don't really wanna do this in mongodb
problem is in templates home index
where we go to each package associated with each release, from where we created that neat reciprocal relationship in sql
to solve this we create a package lookup dicationary that, when given a pckage id, returns the package
this magic is happening in viewmodels home indexviewmodel and package service
n.b you can create variables in jinja, as demoed here
This extra query is very little overhead. Negligibel in this case

### package details cleanup

Again some messing to be done to match the data model, bc the package does not have releases

### concepts

Have to register connections
Create basic classes, all the documents you make will be made on this pattern
Don't have to be limited to tabluar data, instead you can just embed lists in here. It's many to many as well
Simple patterns for search and filter, much more similar syntax to Python 
More details of more advances filtering syntax in here
Remember to do all teh data access before you leave a function. In mongodb, saftest way is to list(response)


