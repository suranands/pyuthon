from sys import argv # not sure what this exactly is. online help everywhere talks about some unpack and all that crap. couldn't make sense.

script,filename = argv # argv takes any number of arguments in it, like a list. here it has 2 arguments. but the first argument is always the name of the file. second argument in this case is a file name. that's all i know.

txt = open(filename) # open() is supposed to open a particular file i guess. but didn't work when i tried.

print "Here's your file %r: " %filename # this is easy, it prints.
print txt.read() # this reads what a text file contains inside, i guess. didn't work again when i tried on terminal and at python prompt.

print "I'll also ask you to type it again:" # simple printing.
file_again = raw_input(">") # taking input from user.

txt_again = open(file_again) # opens the file again, perhaps in the backend?

print txt_again.read() # reads the file again.
