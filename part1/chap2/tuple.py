# tuples as immutable lists
a = (10, 'alpha', [1, 2])
b = (10, 'alpha', [1, 2])

print(a == b)
b[-1].append(3)

print(a == b)
print(b)

# tuples are immutable but if some element of a tuple is mutable, then a tuple can be mutated. 
# In python for homogenous lists, the actual values are stored. For non-homogenous valus, 
# values are referenced. 

# given a tuple t, tuple(t) simply returns a refernce to the tuple. Instead, list(l) must create a
# new copy of l. 

# In python, b, a = a, b swaps the values between a and b. 

# Section: Unpacking sequences
a, b, *rest = range(5)
print(*rest) # equates to [2, 3, 4]
a, *rest, b, c = range(5)
print(*rest) # equates to [1, 2]

# a, b, rest, c = range(5) # throws an error

# remember * is used to unpack lists, tuples and ** for dictionaries. 
# f'{"":15} | {latitide: >9} | {longitude: >9}' - > means right aligned, 15 or 9 means number of characters. 
# f'{name:15} | {lat:9.4f} | {lon:9.4f}' -> 9.4 means 4 decimal places and is included within 9 decimal places. 
# 9.4 works only with floating point numbers.

# Pattern matching with the match/case: 
# def handle_command(self, message): 
# 	case ['LEED', rate, liter): 
#		self.beep(rate, liter) ...

 
# Instances of str, byte, bytearray are not handled as sequences in the context of match/case. 

# The symbol _ is special and can appear more than once in a pattern. 
# case [name, _, _, (lat, lon) as coord]:

name, _, _, lat = ('sumit', 22, 'hello', 'dat')
print(_)      	# prints 'hello'

# case ['lambda', [*params], *body] ensures two levels of capturing the data. 
# case ['lambda', *params, *body] - not allowed and will throw an error. 

# Python slicing: 
s = 'bicycle'
print(s[::3]) # 3 represent stride, s[a:b:c] - start, stop, stride
print(s[::-2])

# Python calls seq.__getitem__(slice(start, stop, step)) when we do slicing s[a:b:c]
# slice can even be assigned to a variable.
sku = slice(2,6,2)
print(s[sku]) # this prints 'cc' 

# in numpy if a is multi-dimensional tensor, then a[i, ...] works instead of a[i,:,:,:,:].
# This doesn't work for standard python. 

l = list(range(10))
print(f'length of l is: {len(l)}')
l[2:6] = [25, 35] # literally replaces element # 2,3,4,5 with 25 and 35. Essentially reduces the length of l. 
print(f'length of modified l is: {len(l)}')
del l[2:5] # deletes those elements
# l[2:4] = 100 # throws an error
l[2:4] = [100] # this works

# Please see the difference between [['_' * 3] for i in range(3)] vs [['_' * 3]] * 3. 
# First one is preferred because second one is equivalent to: x = [['_' * 3] and then a for loop appending the same object x. 
# The first example is actually for i in range(3): x = [['_' * 3]] and append it to a list. A new object is being created at every iteration. 

l = [1, 2, 3] * 3
print(l) 
l[2] = 5
print(l) # [1, 2, 3] is an object 

# in place addition. a += 5 updates the object at a. a = a + 5 doesn't do that - creates a new object if __iadd__ is defined. 
print(id(l))
l *= 2 
print(id(l)) # same id 

t = (1, 2, 3)
print(id(t))
t *= 2
print(id(t)) # different id - because tuples are immutable and hence tuple items has to be copied and then to add new itmes. Rather than copying just create a new one.

# sorted
print('\nStarts the section on sorted') 
x = ['apple', 'mango', 'abc', 'tortoise']
print(sorted(x, key=len))
print(sorted(x, key=len, reverse=True))

# In python, if a function returns None means that the output updated the original object. 

# arrays are very powerful in python.
print('\nBeginning Section on Arrays') 
from array import array 
from random import random

floats = array('d', (random() for i in range(10**7)))
print(floats[-1])

fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()


floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7) 
fp.close()

print(floats2[-1])
print(floats2 == floats)

# memoryview is an important concept in arrays.
numbers = array('h', [-2, -1, 0, 1, 2])
menv = memoryview(numbers)
menv_oct = menv.cast('B')
print(menv_oct.tolist())

menv_oct[5] = 4
print(numbers)

# numpy 
print('Section: Numpy')
import numpy as np
a = np.arange(12)
a.shape = 3, 4
print(a.transpose())

# time counter
floats = np.array([random() for _ in range(10**7)])
print(floats[:3])
from time import perf_counter as pc
t0 = pc(); floats /= 3; pc() - t0
iloats = np.array(random() for _ in range(10**7))
print(floats[:3])
from time import perf_counter as pc
t0 = pc(); floats /= 3; pfloats = np.array(random() for _ in range(10**7))
print(floats[:3])
from time import perf_counter as pc
t0 = pc(); floats /= 3; print(pc() - t0)

# Dequeue
from collections import deque
dq = deque(range(10), maxlen=10)
print(dq)
dq.rotate(1)
print(dq)
dq.appendleft(-7)
print(dq)
dq.extend([11, 6, 19])
dq.extendleft([23, -1, 0])
dq.append(99)
print(dq)

# The algorithm that is used in sorting is called Timsort. This is widely used in list.sort() and in other Android for sorting.










