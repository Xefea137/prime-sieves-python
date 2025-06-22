import numpy as np
import math

def generate_base_primes(limit):
  size = (limit + 1)//2
  is_prime = np.ones(size, dtype=bool)
  is_prime[0] = False
  
  for n in range(1, size):
    if is_prime[n]:
      p = n * 2 + 1
      is_prime[p*p:size:p] = False

  return np.flatnonzero(is_prime) * 2 + 1

def segmented_sieve(start, stop, segment_length):
  if stop < 2:
    return []

  if stop < 3:
    return [2]

  result_primes = []
  if start <= 2:
    result_primes.append(2)

  start = max(start, 3)

  if start % 2 == 0:
    start += 1

  if stop % 2 == 0:
    stop -= 1

  base_primes = generate_base_primes(math.isqrt(stop))
  
  is_prime_segment = np.ones(segment_length, dtype=bool)

  while start <= stop:
    segment_size = min(segment_length, (stop - start)//2 + 1)
    is_prime_segment[:segment_size] = True
    
    for p in base_primes:
      if p * p > start + ((segment_size - 1) * 2):
        break

      first_multiple = max(p * p, ((start + p - 1) // p) * p)
      if first_multiple % 2 == 0:
        first_multiple += p

      start_idx = (first_multiple - start)//2
      if start_idx < segment_size:
        is_prime_segment[start_idx:segment_size:p] = False

    result_primes.extend((np.flatnonzero(is_prime_segment[:segment_size]) * 2) + start)
    start += (segment_size * 2)
  
  return result_primes

start = 999990000
stop = 1000000000
segment_length = 1000000
primes = segmented_sieve(start, stop, segment_length)

print(f"Found {len(primes)} primes")
# print(f"Primes in the range [{start}-{stop}]: ", primes)