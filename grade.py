# Score		Grade
# >= 0.9	A
# >= 0.8	B
# >= 0.7	C
# >= 0.6	D
# < 0.6		F

prompt = 'Enter a score between 0.0 and 1.0: '
i=raw_input(prompt)
try:
	inp = float(i)
	if inp >= 0.9:
		print 'Your Grade is A!'
	elif 0.9>inp>=0.8:
		print 'Your Grade is B!'
	elif 0.8>inp>=0.7:
		print 'Your Grade is C!'
	elif 0.7>inp>=0.6:
		print 'Your Grade is D!'
	elif inp < 0.6:
		print 'Your Grade is F!'
except:
	print 'You need to enter your score, nothing else!'
