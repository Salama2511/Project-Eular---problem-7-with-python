primes = []
def sieve (n):
	digits = [True for i in range (n+1)]

	p = 2 
	while p*p <= n : 
		if digits[p] == True :
			for i in range (p*2 , n+1 , p):
				digits[i] = False
		p = p + 1 

	for p in range (n + 1):
		if digits[p]:
			primes.append(p)

	return primes

sieve(10000000)
print (primes[10001])









