"""Here we implement backend functionality (internal handling of data), which represents the controller
component of the MVC architecture. Associated with it, there is the CRUD paradigm, which states the four
basic operations that any persistent storage of data must implement: Creation, Reading, Updating and
Deleting. We will now implement CUD independently from R.
This app implements the business logic of the inventory of a grocery store."""

items = list() # global variable where we keep the data.

# Creating functionality
def create_items(app_items):
	global items
	items = app_items

def create_item(name, price, qty):
	global items
	items.append({'name' : name, 'price' : price, 'quantity' : qty})


# Reading functionality
def read_item(name):
	global items
	myitems = list(filter(lambda x: x['name']==name, items))
	return myitems[0]

def read_items():
	global items
	return [item for item in items]


'''Actually there are already a couple of problems with this implementation:

1. If you create the same element twice, you get a duplicate in the items list;
2. If you try to read a non-existing item, you get an IndexError exception.

These issues are very easy to fix, but I think it’s important to pause for a moment and think about why they 
are a problem for your application, and how you want to handle these exceptions.

1. duplicate item -> you don’t want duplicates in the list of items. As soon as the user tries to append an 
item that already exists, you want to prevent this operation and return her a message that the item was 
already stored.
2. non-existing item -> obviously you can’t read an item which is not currently available, so you want to 
tell the user that the item is not stored.

It’s important to think about these issues right now because we want to create specific exceptions for these 
situations.
In this example items is just a list, but if it were a table in a SQLite database, these conditions would 
trigger different exceptions (e.g. adding a duplicate could raise an IntegrityError exception). You want to 
create exceptions that are at a higher level of abstraction, and implement the exception handling for each 
persistance layer.

From here, we create the MVC_exceptions file. We will then update this file, which is 
basic_backend_first_implement.py
'''


