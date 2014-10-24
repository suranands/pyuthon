# write a program 
# which repeatedly reads numbers until the user enters 'done'. 
# once 'done' is entered, print out the total, count, and average of the numbers.
# if the user enters anything other than a number or done,
# detect their mistake using try and except 
# and print an error message and skip to the next number.

try:
	l = []
	maxLengthList = 20
	while len(l) < maxLengthList:
		n = int(raw_input('Enter a number: '))
		l.append(n)
		print l
		if n == "Done" or n == "DONE" or n == "done":
        	    print "Done!"
		break

count = len(l)
total = 0
average = 0
for n in l:
	count = count + 1
	n + n
	total = total + n
	average = (total + n) / count
print 'Count: ',count
print 'Total: ',total
print 'Average: ',average

except:
        n = int(raw_input('Invalid Input! Enter a number: '))
