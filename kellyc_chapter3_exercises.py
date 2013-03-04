# Exercises for chapter 3: Problems 3.1, 3.2, 3.3, and 3.4 in Think Python

# Kelly Chiang

#3.1 
#NameError: name 'repeat_lyrics' is not defined
repeat_lyrics()

def print_lyrics():
print "I'm a lumberjack, and I'm okay."
print "I sleep all night, and I work all day."

def repeat_lyrics():
print_lyrics()
print_lyrics()

#3.2 
# NameError: global name 'print_lyrics' is not defined

def repeat_lyrics():
	print_lyrics()
	print_lyrics()

repeat_lyrics()

def print_lyrics():
	print "I'm a lumberjack, and I'm okay."
	print "I sleep all night, and I work all day. :)"

#3.3

def right_justify(s):
     print s.rjust(70) 

right_justify('bubbletea')

#3.4
#1) empty parentheses indicate function takes no arguments
def do_twice(f):
    f()
    f()

def print_spam():
    print 'spam'

do_twice(print_spam)

#2) print_spam rolls up into f(a)

def do_twice(f, a):
    f(a)
    f(a)

def print_spam(a):
    print a

do_twice(print_spam, 'bubbletea')


#3) 
def print_twice(a):
    print(a)
    print(a)

song = 'la dee da doop dee doo'
print_twice(song)


#4)
def do_twice(f, a):
    f(a)
    f(a)

def print_twice(spam):
    print spam
    print spam

do_twice(print_twice, 'bubbletea')

#5) Define a new function called do_four that takes a function object and a value and calls the function four times, passing the value as a parameter. There should be only two statements in the body of this function, not four.

def do_twice(f, a):
    f(a)
    f(a)

def print_twice(spam):
    print spam
    print spam

def do_four(f,a):
    do_twice(f, a)
    do_twice(f, a)

do_four(print_twice,'spam')
print 'spam'



