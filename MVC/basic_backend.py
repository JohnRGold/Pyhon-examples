"""Now, in this file, unlike in basic_backend_first_implement.py, if you try to create an item that already
exists, you get a ItemAlreadyStored exception, and if you try to read an item that is not stored, you get a
ItemNotStored exception."""
import MVC.MVC_exceptions as mvc_exc

items = list() # global variable where we keep the data.

# Creating functionality
def create_item(name, price, qty):
	global items
	results = list(filter(lambda x: x['name']==name, items))
	if results:
		raise mvc_exc.ItemAlreadyStored('{} already stored'.format(name))
	else:
		items.append({'name' : name, 'price' : price, 'quantity' : qty})

def create_items(app_items):
	global items
	items = app_items


# Reading functionality
def read_item(name):
	global items
	myitems = list(filter(lambda x: x['name']==name, items))
	if myitems:
		return myitems[0]
	else:
		raise mvc_exc.ItemNotStored('Can\'t read {} from list because it is not stored'.format(name))

def read_items():
	global items
	return [item for item in items]


'''Let us now implement functionality for Updating and Deleting'''
# Updating functionality
def update_item(name, price, qty):
	global items
	# Python 3 removed tuple parameters unpacking
	idxs_items = list(
		filter(lambda i_x: i_x[1]['name']==name, enumerate(items)))
	if idxs_items:
		i, item_to_update = idxs_items[0][0], idxs_items[0][1]
		items[i] = {'name' : name, 'price' : price, 'quantity' : qty}
	else:
		raise mvc_exc.ItemNotStored('Can\'t read {} from list because it is not stored'.format(name))

# Deleling functionality
def delete_item(name):
	global items
	idxs_items = list(
		filter(lambda i_x: i_x[1]['name']==name, enumerate(items)))
	if idxs_items:
		i, item_to_update = idxs_items[0][0], idxs_items[0][1]
		del items[i]
	else:
		raise mvc_exc.ItemNotStored('Can\'t read {} from list because it is not stored'.format(name))


# WE NOW ADD MAIN COMPONENT TO TEST THESE FUNCTIONALITIES
def main():
	my_items = [
		{'name': 'bread', 'price': 0.5, 'quantity': 20},
		{'name': 'milk', 'price': 1.0, 'quantity': 10},
		{'name': 'wine', 'price': 10.0, 'quantity': 5},
	]

	# CREATE
	create_items(my_items)
	create_item('beer', price=3.0, qty=15)
	# if we try to re-create an object we get an ItemAlreadyStored exception
	# create_item('beer', price=2.0, quantity=10)

	# READ
	print('READ items')
	print(read_items())
	# if we try to read an object not stored we get an ItemNotStored exception
	# print('READ chocolate')
	# print(read_item('chocolate'))
	print('READ bread')
	print(read_item('bread'))

	# UPDATE
	print('UPDATE bread')
	update_item('bread', price=2.0, qty=30)
	print(read_item('bread'))
	# if we try to update an object not stored we get an ItemNotStored exception
	# print('UPDATE chocolate')
	# update_item('chocolate', price=10.0, quantity=20)

	# DELETE
	print('DELETE beer')
	delete_item('beer')
	# if we try to delete an object not stored we get an ItemNotStored exception
	# print('DELETE chocolate')
	# delete_item('chocolate')

	print('READ items')
	print(read_items())


if __name__ == '__main__':
	main()


'''Now that all CRUD operations are implemented as simple functions, it’s very easy to “package” them into a 
single class. As you can see, there is no mention of View or Controller in the ModelBasic class.'''
