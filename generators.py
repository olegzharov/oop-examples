# seq 1 to 9 000 000
# LAZY
import sys


def mygenerator(n):
    for x in range(n):
        yield x ** 3

values = mygenerator(100)

for x in values:
    print(x)
#print(next(values))
print(sys.getsizeof(values))