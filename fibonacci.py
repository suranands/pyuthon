# Fibonacci series:
# Fn = Fn-1 + Fn-2
# the sum of two elements defines the next
a,b=0,1
while b<1000:
	print(b,end=',')
	a,b = b, a+b

