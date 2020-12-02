#import numpy as np
'''
Describing the use of the "enumerate" function to make for loop ranges far cleaner and more pythonic than the usual "for indx in range(len(A))" syntax.
Obviously, though, this only applies to loops through iterable objects. Looping through a range of a computed size N may not be doable with this logic.
'''

L = [43,32,64,74,13,46]

for i, element in enumerate(L):
	print(i,element)
	# enumerate returns tuples with index and object value in the iterable object L (enumerate works only with objects within the class iterable for obvious reasons)
print('\n')

for i, element in enumerate(L,1):
	print(i,element)
	# this extra argument in enumerate creates a synthetic indexing that replaces the usual 0-indexing that is default in Python. Thus, the same elements will be printed, only indexed from 1 to N
	# instead of the usual 0 to N-1
print('\n')

for _, element in enumerate(L,1):
	print(element)
	# this "I don't care" use of the underscore is fully supported within the enumerate function. That way enumerate only returns singlets instead of tuples
	# incidentally, this is the actual logic behind the for x in object syntax stated below
print('\n')

for element in L:
	print(element)
	# this is a verbose-free version of the previous example. When the index is fully omitted, enumerate() also becomes unnecessary and Pyhon implicitly does it right as long as L is an iterable
print('\n')

pisos = ['sotano', 'bajo', 'primero', 'segundo', 'atico']
for k, name in enumerate(pisos, -1):
	print(name,k)

while _ !=0:
	print(_)
	# EXTREMELY UNSETTLING. _ remains defined after having been used in a previous for loop. Upon loop termination, index and value variable names are kept to their last value.
	# Surprisingly, this is also the case for _. If you print it here, _ will return the last value it took in line 20, that is 6, since you did enumerate(L,1) and L has 6 elements.