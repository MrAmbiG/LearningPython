'''
http://book.pythontips.com/en/latest/context_managers.html
https://www.youtube.com/watch?v=-aKFBoZpiqA
https://www.guru99.com/reading-and-writing-files-in-python.html#2
'''

# create a file if not present
file_name = 'my_file.txt'
f = open(file_name, 'w+')
f.close()  # close once done

# open file_name
f = open(file_name, 'a+')  # open file in append mode
f.write('python rules')
f.close()

'''
w - write mode
r - read mode
a - append mode
+ to any of the above means open them in that mode
and create file if it is not present
'''

'''
w  write mode
r  read mode
a  append mode

w+  create file if it doesn't exist and open it in write mode
r+  create file if it doesn't exist and open it in read mode
a+  create file if it doesn't exist and open it in append mode
'''

f = open(file_name, 'a+')  # open file in append mode

try:
    f.write('python rules')
finally:
    f.close()


'''
Context managers allow you to lock, unlock resources like a file, database
connection etc., This is mostly implemented as a class
'''


class Resource(object):
    def __init__(self):
        pass

    def __enter__(self):  # opens the file
        pass

    def __exit__(self):  # close the file
        pass


'''
Above is a barebone structure of a context manager class which you want
to start with...
'''

'''the goal is to make sure the file is closed once the task is done.
The same can be done easily by using with'''

# with open(file_name, 'w+') as f:
#     print(f.closed)
#     f.write('I rule')
#     print(f.closed)
# print(f.closed)

# context manager as a class


# class myFile(object):
#     def __init__(self, filename, method):
#         self.filename = filename
#         self.method = method
#
#     def __enter__(self):
#         self.f = open(self.filename, self.method)
#         return self.f  # opens the file
#
#     def __exit__(self, type, value, traceback):
#         self.f.close()  # close the file
#         return True
#
#
# with myFile(file_name, 'w') as pyFile:
#     pyFile.write('hey')
#
# print(pyFile.closed)  # so the file is closed which means no errors occured
'''
if there is a problem with this process then the type, value and traceback
of the error are passed down to the user.
'''
# context manager as a generator
from contextlib import contextmanager


@contextmanager
def myFile(name):
    try:
        f = open(name, 'w+')
        yield f
    finally:
        f.close()


with myFile(file_name) as f:
    f.write('hey')

print(f.closed)

'''
you can use this method of set up and tear down of resources
when you are dealing with databases. Let us say you have
to run some commands against a database. The procedure involves
atleast 3 steps
1. connect to database
2. run commands
3. close connection to database
Using context managers you can save a lot of code, time and be efficient
by offloading the step1 and step3 to context managers so that whenever
you do step2 the context manager will do the step1 and step3 for you.
'''
