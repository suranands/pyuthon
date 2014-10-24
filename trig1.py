import math
degrees = float(raw_input('Enter the value to be converted into radians: '))
radians = degrees / 360.0 * 2 * math.pi
print '%f Radians' %radians
print 'Sine %.02f degrees is %f.' %(degrees,math.sin(radians))
print 'Cosine %.02f degrees is %f' %(degrees,math.cos(radians))
print 'Tangent %.02f degrees is %f' %(degrees,math.tan(radians))

# trignometric functions like sin, cos, tan, etc. take arguments only in radians.

