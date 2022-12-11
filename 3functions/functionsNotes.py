# we can refer to global variables in functions by
# speceifying the variable with 'global'
def spam():
	global eggs
	eggs = 'spam'


def bacon():
	eggs = 'bacon'
	print(eggs)


eggs = 'global'
spam()
print(eggs)

# functions are usually described as black boxes
# as knowing what happens inside of them
# are usually irrelevant to the task at hand,
# and we place faith in whoever programmed it

# Exception handling
# use 'try:' and 'exception ___:'
def divide42(numb):
	try:
		return 42 / numb
	except ZeroDivisionError:
		print('error invalid argument')


print(divide42(0))

# alternatively
def altDivide42(numb):
	return 42 / numb
try:
	print(altDivide42(2))
	print(altDivide42(0))
	print(altDivide42(3))
except ZeroDivisionError:
	print('eerorr')

