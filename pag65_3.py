# write a program 
# which repeatedly reads numbers until the user enters 'done'. 
# once 'done' is entered, print out the total, count, and average of the numbers.
# if the user enters anything other than a number or done,
# detect their mistake using try and except 
# and print an error message and skip to the next number.

l = []
inp = 'Enter a number: '

while True:
	s = raw_input(inp)
	l.append(s)
        print l
        if s == 'done':
                break
        try:
                minm = min(l)
                maxm = max(l)
        except ValueError:
                print "Invalid Input. Try again: "
		continue
print "Here is your list\n %s\n whose largest is %s\n and smallest is %s.\n" % (l,str(maxm), str(minm))


