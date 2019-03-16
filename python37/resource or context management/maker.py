file='1file.txt'
f=open(file, 'w')
f.write('hello\n')
f.close()

# writes to a file

'''
w  write mode
r  read mode
a  append mode

w+  create file if it doesn't exist and open it in write mode
r+  special read and write mode
a+  create file if it doesn't exist and open it in append mode
'''
file='2file.txt'
f=open(file, 'w+')
f.write('hello\n')
f.close()

'''w or w+ keeps overwriting the same file'''
file='3file.txt'
f=open(file, 'a+')
f.write('hello\n')
f.close()
'''a or a+ keeps appending'''

## read everything
file='3file.txt'
f=open(file, 'r')
data=f.read()
print(data)

## choose how much to read
file='3file.txt'
f=open(file, 'r')
data=f.read(2) # first 2 characters only
print(data)
print('---------')
data=f.read(5) # next 5 characters only (/n is also a character)
print(data)

## read line by line
file='4file.txt'
f=open(file,'a+')
f.write('line1\nline2\nline3\nline4\nline5\n')
f.close()

file='4file.txt'
f=open(file,'r')
print(f.readlines())
f.close()

## looping through lines
file='4file.txt'
f=open(file,'r')
for line in f.readlines():
    print(line)
f.close()

## With statement
file='4file.txt'
with open(file, 'r+') as f:
    f.write('something\n')
    print(f.read())
    print(f.closed) # within the with statement the file is always open
print(f.closed) # once you come out of the with statement the file gets closed

'''
Context managers allow you to lock, unlock resources like a file, database
connection etc., This is mostly implemented as a class
Below is a barebone structure of a context manager class which you want
to start with...
'''
class Resource(object):
    def __init__(self):
        pass

    def __enter__(self):  # opens the file
        pass

    def __exit__(self):  # close the file
        pass
'''the goal is to make sure the file is closed once the task is done.
The same can be done easily by using with'''
file='4file.txt'
with open(file, 'w+') as f:
    print(f.closed)
    f.write('I rule')
    print(f.closed)
print(f.closed)

# context manager as a class
class myFile(object):
    def __init__(self, filename, method):
        self.filename = filename
        self.method = method

    def __enter__(self):
        self.f = open(self.filename, self.method)
        return self.f  # opens the file

    def __exit__(self, type, value, traceback):
        self.f.close()  # close the file
        return True
#
#
file='5file.txt'
with myFile(file, 'w+') as pyFile:
    pyFile.write('hey')

print(pyFile.closed)  # so the file is closed which means no errors occured

'''
if there is a problem with this process then the type, value and traceback
of the error are passed down to the user as shown below
'''
with myFile(unknownfile, 'w+') as pyFile:
    pyFile.write('hey')

## context manager as a generator
from contextlib import contextmanager

@contextmanager
def myFile(name):
    try:
        f = open(name, 'w+')
        yield f # acts as a generator instead of as a normal function
    finally:
        f.close()


file_name='4file.txt'
with myFile(file_name) as f:
    f.write('hey')

print(f.closed)

## lock and unlock
from threading import Lock
lock = Lock()

def do_stuff():
    lock.acquire()
    raise Exception('got an error')
    lock.release()

try:
    do_stuff()
except Exception as e:
    print(e)
lock.acquire()
print('Got here')

def do_stuff():
    with lock:
        raise Exception('got an error')

try:
    do_stuff()
except Exception as e:
    print(e)
lock.acquire()
print('Got here')
