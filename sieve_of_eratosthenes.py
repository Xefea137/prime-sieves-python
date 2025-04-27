import math
import numpy as np

def sieve_of_eratosthenes(upper_limit, file_name=None):
  size = (upper_limit + 1) // 2
  isPrime = np.ones(size, dtype=bool)
  isPrime[0] = False

  sqRt = math.isqrt(upper_limit)
  for n in range(3, sqRt + 1, 2):
    if isPrime[n//2]:
      start = (n*n)//2
      isPrime[start::n] = False

  prime = np.concatenate(([2], 2 * np.flatnonzero(isPrime) + 1))
  
  if file_name:
    np.savetxt(file_name, prime, fmt='%d')
  
  return prime

upper_limit = 1000000000
file_name = None
primes = sieve_of_eratosthenes(upper_limit, file_name)
# print(f"Found {len(primes)} primes. First 10 primes: {primes[:10]}")