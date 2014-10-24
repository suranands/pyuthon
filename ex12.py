from sys import argv

script, filename = argv
print "Script:",script # prints script name
print "Filename:",filename # prints the first argument

filename = argv
print "Filename:",filename # prints something like ["my-script.py","my-file.txt"]
