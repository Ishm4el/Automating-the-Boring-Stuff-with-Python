import random

# removing an element from a list:
myItems = ['cat', 'dog', 'bat']
print(myItems)
del myItems[0]
print(myItems)

print()
# the 'in' and 'not in' operators allow us to determine whether a value is in a list
print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])

print()
# Multiple assignment is possible in python:
cat = ['fat', 'gray', 'loud']
size, color, disposition = cat
print(size, color, disposition)

print()
# enumerate() : will return two values with a for loop and a list. it will return the index and an item from the list.
for index, aCat in enumerate(cat):
    print('index: ' + str(index) + ', cat: ' + aCat)

# random.choice() and random.shuffle()
# random.choice() will pick a random item from a list
print(random.choice(cat))
# This is equivalent to:
print(cat[random.randint(0, len(cat) - 1)])
print(cat)
random.shuffle(cat)
print(cat)

print()
# index() : we can use to identify the index of an item
print(cat.index('loud'))

# .append() and .instert
# alternatives to adding values to a list.
# append will add to the end a list
# insert will insert at a designated index
cat.append('Lili')
cat.insert(0, 'hilda')
print(cat)

print()
# remove()
# will remove vlaues from a list
cat.remove('hilda')
print(cat)
# Alternatively, we can use:
# del object[index]
del cat[-1]

# .sort()
# will sort a list
print()
cat.sort()
print(cat)
# .sort(reverse=True)
cat.sort(reverse=True)
print(cat)
# by default, sort will order by asci descending
# alternatively, we can sort by true alphabetical order
cat.sort(key=str.lower)
print(cat)

# .reverse()
# will reverse the order of a list
print()
print('reverse the order of cat')
cat.reverse()
print(cat)

# Sequence Data Types
# The Python sequence data types incude:
# lists, strings, range objects returned by
# range(), and tuples, which includes the ability to:
# indexing, slicing, and using them with for loop, with
# len(), and with the 'in' and 'not in' operators.
print('\nSequence Data Types')
name = 'Zophie'
print(name[0])
print(name[-2])
print(name[0:4])
print('Zo' in name)
print('z' in name)
print('p' not in name)
for i in name:
    print('* * * ' + i + ' * * * ')
print()

# The Tuple Data Type
"""
The tuple data type is almost identical to the list data type, except in two ways. First, tuples are typed with parentheses, '(' and ')', instead of square brackets, '[' and ']'
"""
eggs = ('hello', 42, 0.5)
print(eggs)
print(eggs[0])
print(eggs[1:3])
print(len(eggs))
# The unique aspect of tuples in comparison
# to lists is that tuples cannot:
# mutate
# modified, appended, or removed.
# ~
# In order to specify a tuple we
# may add a comma at the end if 
# our tuple only has a single item
print("type('hello',)")
print(type('hello',))
print()

# Converting types with list() and tuple() functions
tupleCat = tuple(cat)
print(tupleCat)
print(type(tupleCat))
print()
reverseCat = list(tupleCat)
print(reverseCat)
print(type(reverseCat))
print()



