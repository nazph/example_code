
import itertools

def loop_simul(list1, list2):
	for x, y in zip(list1, list2):
		print x, y

list1 = [(2,30, 5), (3, 6, 7), (6, 4, 9)]
list2 = [11, 355, 678]

loop_simul(list1, list2)