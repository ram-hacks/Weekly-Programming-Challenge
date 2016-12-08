#!/usr/bin/env python

# DO NOT EVER WRITE CODE LIKE THIS
f=lambda l:(lambda n:reduce(lambda a,b:a^b,l)^[n,1,n+1,0][n%4])(len(l)+1)

if __name__ == '__main__':
	from random import sample
	assert f([7,8,10,3,6,5,1,2,9]) == 4
	assert f([1,3]) == 2
	n = 10000
	for i in range(10):
		l = sample(range(1,n+1),n-1)
		assert(sorted(l + [f(l)]) == range(1,n+1))
