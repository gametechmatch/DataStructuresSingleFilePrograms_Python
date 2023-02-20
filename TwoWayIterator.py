#################################################################
# TwoWayIterator.py
#################################################################
# Author: gametechmatch
# Course: Data Structures
# CH5 - Linked Lists
# HW3 - WK3
# Programming Project 5.7
#################################################################
# This file contains an iterator class that can move forward
# and backward. At the end, it tests the different methods
# with the Fibonacci sequence filled into a list (array)
#################################################################

class TwoWayIterator(object):
	# This method initializes the iterator
	def __init__(self, value):
		self.value = value
		self.iter = None
		self.index = 0

	# This method moves forward through the values by one step
	def next(self):
		# Raise the StopIteration error if next = None
		try:
			result = self.value[self.index]
			self.index += 1
		except IndexError:
			raise StopIteration #Raise StopIteration if past end
		return result

	# This method moves backward through the values by one step
	def previous(self):
		self.index -= 1
		if self.index < 0:
			raise StopIteration #Raise StopIteration if past beginning
		return self.value[self.index]

	def __iter__(self):
		return self

# Execute main method
if __name__ == '__main__':
	# Create an iterator for a list of fibonacci numbers
	the_fib_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21]
	my_iterator = TwoWayIterator(the_fib_sequence)

	# test TwoWayIterator methods
	print("forward")
	print(my_iterator.next())
	print(my_iterator.next())
	print(my_iterator.next())
	print(my_iterator.next())
	print("backward")
	print(my_iterator.previous())
	print("forward")
	print(my_iterator.next())
	print(my_iterator.next())
	print("backward")
	print(my_iterator.previous())
	print(my_iterator.previous())
	print(my_iterator.previous())
	print(my_iterator.previous())
	print(my_iterator.previous())
	print(my_iterator.previous())
