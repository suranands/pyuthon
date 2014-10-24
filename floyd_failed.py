# Python Program to print a Floy's triangle
# This code is copied from
# http://rosettacode.org/wiki/Floyd's_triangle#Python

def floyd(rowcount=5):
	rows = [[1]]
	while len(rows) < rowcount:
		n = rows[-1][-1] + 1
		rows.append(list(range(n, n + len(rows[-1]) + 1)))
	return rows
 
floyd()
[[1], [2, 3], [4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14, 15]]

def pfloyd(rows=[[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]):
	colspace = [len(str(n)) for n in rows[-1]]
	for row in rows:
		print( ' '.join('%*i' % space_n for space_n in zip(colspace, row)))
 
