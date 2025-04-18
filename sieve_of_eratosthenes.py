import numpy as np

np.set_printoptions(threshold=np.inf)

upper_limit = 1000000

isPrime = np.ones(upper_limit, dtype=bool)
isPrime[0:2] = False

sqRt = int(np.sqrt(upper_limit)) + 1

for n in range(2, sqRt):
  if isPrime[n]:
    isPrime[n*n:upper_limit:n] = False

prime = np.flatnonzero(isPrime)

if prime[13] == 43:
  print("OKAY")

print(prime)

np.savetxt('primes.txt', prime, fmt='%d')