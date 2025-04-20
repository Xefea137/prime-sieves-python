import math
import numpy as np
# np.set_printoptions(threshold=np.inf)

def sieve_of_eratosthenes(upper_limit, file_name=None):
  isPrime = np.ones(upper_limit, dtype=bool)
  isPrime[0:2] = False

  sqRt = math.isqrt(upper_limit)
  #sqRt = int(np.sqrt(upper_limit)) + 1
  for n in range(2, sqRt+1):
    if isPrime[n]:
      isPrime[n*n:upper_limit:n] = False

  prime = np.flatnonzero(isPrime)
  
  if file_name:
    np.savetxt(file_name, prime, fmt='%d')
  
  return prime

upper_limit = 100000000
file_name = None #'primes.txt'
primes = sieve_of_eratosthenes(upper_limit, file_name)
# print(primes)