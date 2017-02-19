#basic generators
def generators(n):
    yield n
    yield n + n
    yield n * n

gen = generators(6)

next(gen) # return 6
next(gen) # return 12
next(gen) # return 36


#Generators expression
gex = (n for n in range(10))

next(gex) # return 0
next(gex) # return 1

gen = (n * n for n in range(5, 9))

next(gen) # return 25
next(gen) # return 36
next(gen) # return 49

gen = (n ** 2 for n in range(10) if n % 2 == 0)

next(gen) # return 0
next(gen) # return 4
next(gen) # return 16
next(gen) # return 36
next(gen) # return 64

#Fib Generators

def fib(num):
	a, b = 0, 1

	for i in range(0, num):
		yield '{}: {}'.format(i + 1, a)
		a, b = b, a + b

for item in fib(10):
	print(item)