# numpy. 
# import numpy as np 
# create an array



import numpy
a= numpy.array([1,2,3,4])
print(a)


# question
import numpy as np
np_arr = np.array([3,3,3,3,3.3,'hello',False])
print(bool(np_arr[-1]))
# store only one type of data (if diffrent than that data will be stored as string )
# output: true
# true because false is taken as string because of "hello" and string is a value in itself so a value is true always

a= False
print(bool(a))



# zero<--- gives zeros in array
a = np.zeros(3)
print(a)

# matricex or 2D or 3D ARRAY
a = np.zeros((2,3,4))
print(a)


# ones <-- ones only
a=np.ones(3)
print(a)



# empty <-----[garbage value]
a=np.empty(3,dtype=int)
print(a)



# full <--- create array with any value
a= np.full(4,5,dtype=int)
print(a)




# arrange () &  linspace()
import numpy as np

# arange
a = np.arange(3, 12, 1)
print(a)

# linspace
b = np.linspace(3, 12, 4)
print(b)



# Tells you the dimensions of the array.

import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(a.shape)




# Tells you the total number of elements in the array.

import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(a.size)






# Generates random integers within a given range.

import numpy as np

print(np.random.randint(1, 10))





# Randomly selects value(s) from a list or array.

import numpy as np

fruits = ["Apple", "Mango", "Banana"]

print(np.random.choice(fruits))





#  operation on array with same size
# broadcasting<---- Broadcasting allows NumPy to perform operations on arrays of different shapes without manually resizing them.
# NumPy can broadcast if:
#1. Dimensions are equal, or
#2.One of the dimensions is 1
import numpy
a= numpy.array([1,2,3,4])
b= numpy.array([8,5,7,8])
print(a+b)
print(a*b)
print(a/b)
print(a-b)



# reshape() <-- is used to change the shape (dimensions) of an array without changing its data.

import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])

b = a.reshape(2, 3)

print(b)

# example

a = np.array([1, 2, 3, 4, 5, 6, 7, 8])

b = a.reshape(2, 2, 2)

print(b)




# transpose()<---is used to swap rows and columns of an array.
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])
print(a)

b = a.transpose()
print(b)





# concatenate() is used to join two or more arrays into a single array.
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.concatenate((a, b))
print(c)





# concaenate
# Join Columns (axis=1)
import numpy as np

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

c = np.concatenate((a, b), axis=1)

print(c)






# concatenate
# Join Rows (axis=0)
import numpy as np

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

c = np.concatenate((a, b), axis=0)

print(c)






#  question ---- analyse score
import numpy as np

scores = []

days = ["Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"]

for day in days:
    score = int(input(f"Enter score for {day}: "))
    scores.append(score)

scores = np.array(scores)

print("Scores:", scores)
print("Maximum Score:", np.max(scores))
print("Minimum Score:", np.min(scores))
print("Average Score:", np.mean(scores))
print("Standard Deviation:", np.std(scores))