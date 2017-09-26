from sys import stdin

n,m = map(int,next(stdin).split())
while n and m:
	a = [int(next(stdin)) for _ in xrange(n)]
	shared, i = 0, 0
	for _ in xrange(m):
		b = int(next(stdin))
		while i+1 < n and b > a[i]:
			i+=1
		shared += b == a[i]
	print shared
	n,m = map(int,next(stdin).split())
