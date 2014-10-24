inp = raw_input('Enter Fahrenheit Temperature: ')
try:
	fahr = float(inp)
	cel = (fahr-32) * 5/9
	print cel
except:
	 print 'Please enter a number: '

