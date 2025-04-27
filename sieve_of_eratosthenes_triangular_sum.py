import math
import numpy as np

def sieve_of_eratosthenes(upper_limit, file_name=None):
  size = upper_limit // 2 + 1
  isPrime = np.ones(size, dtype=bool)
  isPrime[0] = False

  sqRt = math.isqrt(upper_limit)

  triangular_sum = 0
  for n in range(1, sqRt//2 + 1):
    triangular_sum += n
    if isPrime[n]:
      x = (n * 2) + 1
      isPrime[4*triangular_sum::x] = False

  prime = np.concatenate(([2], 2*np.flatnonzero(isPrime)+1))
  
  if file_name:
    np.savetxt(file_name, prime, fmt='%d')
  
  return prime

upper_limit = 100000000
file_name = None
primes = sieve_of_eratosthenes(upper_limit, file_name)
# print(f"Found {len(primes)} primes. First 10 primes: {primes[:10]}")