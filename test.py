'''
The code below test the solution with the given list [2,3,6,6,5]
'''
# n = int(input())  # gets input from command line and converts it into an integer
my_array = map(int, [2, 3, 6, 6, 5])  # map input to int
# convert array to list, get its set then convert it into a list
my_array = list(set(list(my_array)))
# The lines below sorts the the list and gets it's second last element then prints it out
ar = len(my_array)
my_array = sorted(my_array)
print(my_array[ar-2])
