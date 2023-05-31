import numpy as np
from io import StringIO

#print(np.__version__) checks version of NumPy

'''
array = np.arange(10) #create array with numbers 1 through 9
secondElement = array[-1] #negative index counts backwards
print(secondElement)

'''

'''
array2d = np.random.rand(4, 3)
print(array2d)
element2d = array2d[0,0]
print(element2d)

'''

#print(array[2])

'''
vanillarray = [0, 1, 2, 3, 4, 5]
print(vanillarray[2])

'''

'''

# create a 2D array with 3 rows and 4 columns using nested lists
my_matrix = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12]]

# access a single element at row 1, column 2 (i.e., element with value 7)
print(my_matrix[1][2])

# access a row (i.e., second row)
print(my_matrix[1])

# access a column (i.e., third column)
print([row[2] for row in my_matrix])

# access a sub-matrix (i.e., first two rows and first three columns)
print([row[:3] for row in my_matrix[:2]])

'''
'''
data = u"1, 2, 3\n4, 5, 6"
ioarray = np.genfromtxt(StringIO(data), delimiter=",", skip_header=0, skip_footer=0, 
                 converters=None, missing_values=None, filling_values=None, usecols=None, 
                 names=None, excludelist=None, deletechars=None, replace_space='_', 
                 autostrip=False, case_sensitive=True, defaultfmt='f%i', unpack=None, 
                 usemask=False, loose=True, invalid_raise=True, max_rows=None, encoding='bytes')

print(ioarray)

'''


'''

list1 = [1, 2, 3]

list2 = [[10],
		[20],
		[30]]

vector1 = np.array(list1)
vector2 = np.array(list2)

print("Horizontal Vector")
print(vector1)

print("Vertical Vector")
print(vector2)

'''

list1 = [1, 2, 3]

list2 = [10,20,30]

vector1 = np.array(list1)
vector2 = np.array(list2)

addVectors = vector1 + vector2
print(addVectors)

subtractVectors = vector1 - vector2
print(subtractVectors)

multiplyVectors = vector1 * vector2
print(multiplyVectors)

divideVectors = vector1 / vector2
print(divideVectors)



















