import sys
import getopt   # for optional arguments
#def myfunction(*args, **kwargs):
# sys.argv[0] - name
# sys.argv[1] - params ...
# Usage: main.py -p 8080 -h localhost
# optional arguments
# можно использовать флаги
# f_flag = True
# m_flag = True
filename = 'test.txt'
message = 'Hello world!'

opts, args = getopt.getopt(sys.argv[1:],"f:m:", ['filename', 'message'])
print(opts)
print(args)
for opt, arg in opts:
    if opt == '-f':
        filename = arg
    if opt == '-m':
        message = arg
print(filename, message)
# oleg-zharov@oleg-zharov-nix:~/y/py/tmp/oop-examples$ python arguments-parsing.py -f test.txt -m Hello
# [('-f', 'test.txt'), ('-m', 'Hello')]

# filename = sys.argv[1]
# message = sys.argv[2]
#with open(filename, 'w+') as f:
#     f.write(message)
#

