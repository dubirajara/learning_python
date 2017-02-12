#basic generators
def generators(n):
    yield n
    yield n + n
    yield n * n

gen = generators(6)

next(gen) # return 6
next(gen) # return 12
next(gen) # return 36

