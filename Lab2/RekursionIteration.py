import math

def bounce(n: int):
	"""Prints numbers n-0-n using recursion"""
	print(n)
	if n > 0:
		bounce(n - 1)
		print(n)

def bounce2(n):
	"""Prints numbers n-0-n using iteration"""
	for x in range(-n, n + 1):
	    print(abs(x))

def tvarsumman(n):
	"""Prints sum of digits in number n using recursion"""
	x = n % 10
	if n > 0:
		x += tvarsumman(n // 10)
	return x

def tvarsumman2(n):
	"""Prints sum of digits in number n using iteration"""
	x = 0
	while n > 0:
		x += n % 10
		n = n // 10
	return x

def derivative(f, x, h):
	"""Returns derivative of function f, at point x, with precision h"""
	return float((1 / (2 * h)) * (f(x + h) - f(x - h)))

def solve(f, x0, h):
	"""Returns the first x-axis intersection of function f, with starting point x0, precision h"""
	xPrev = x0 + h	#Add h to avoid an immediate division with zero
	while True:
		xNext = xPrev - (f(xPrev) / derivative(f, xPrev, h))
		#Calculate intersection using Newton-Raphson's method
		#Don't ask me to explain it, I just programmed the dang thing
		
		if (abs(xPrev - xNext) <= h): #Return if calculation reaches convergence
			return xNext
		else:
			xPrev = xNext

def testFunction(x):
	return x**2 - 1



