# write a program 
# which repeatedly reads numbers until the user enters 'done'. 
# once 'done' is entered, print out the total, count, and average of the numbers.
# if the user enters anything other than a number or done,
# detect their mistake using try and except 
# and print an error message and skip to the next number.

inp = 'Enter a number: '
total = 0
count = 0

while True:
        s = raw_input(inp)
        if s == 'done':
                break
        try:
                total += float(s)
                count += 1
        except ValueError:
                print "Invalid Input. Try again: "
		continue
print 'You entered %s numbers whose total is %s and average is %s.' % (str(count), str(total), str(total/count))


