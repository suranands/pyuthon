# This is an example for integration using python.
# Copied from http://docs.scipy.org/doc/scipy/reference/tutorial/integrate.html
import scipy as sp
result = integrate.quad(lambda x: special.jv(2.5,x),0,4.5)
print result
