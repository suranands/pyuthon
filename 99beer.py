# exercise from http://www.ling.gu.se/~lager/python_exercises.html
# solution from http://rosettacode.org/wiki/99_Bottles_of_Beer#Python

# "99 bottle of beer" is a traditional song in the US and Canada.
# it is popular to sing on long trips, as it has a very repetitive
# format which is easy to memorize, and can take a long time to sing.
# the song's simple lyrics are as follows:
# 	99 bottles of beer on the wall, 99 bottles of beer.
# 	take one down, pass it around, 98 bottles of beer on the wall.
# the same verse is repeated, each time with one fewer bottle.
# the song is completed when the singers reach zero.
# Task now is to write a Python program 
# capable of generating all the verses of the song.

print '------------------------------'
print '99 Bottles of Beer on the Wall'
print '------------------------------'

bottles = 99
song = '''
	%d bottles of beer on the wall, %d bottles of beer.\n
	Take one down, pass it around, %d bottles of beer.
	'''

for bottles in range(99,0,-1):
	print song %(bottles,bottles,bottles-1)
