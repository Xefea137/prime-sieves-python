import numpy as np
import math

def segmented_sieve(start, stop, chunk_size):
  if stop < 2:
    return []

  if stop < 3:
    return [2]

  start = max(start, 2)

  sqrt = math.isqrt(stop)
  base_sieve = np.ones(sqrt + 1, dtype=bool)
  base_sieve [[0, 1]] = False

  for n in range(2, sqrt+1):
    if (base_sieve [n]):
      base_sieve[n * n:sqrt + 1:n] = False

  base_primes = np.flatnonzero(base_sieve)

  segment_start = start
  all_primes = []
  is_prime_segment = np.ones(chunk_size, dtype=bool)

  while segment_start < stop:
    segment_size = min(chunk_size, stop - segment_start + 1)
    is_prime_segment[:segment_size] = True

    for p in base_primes:
      if p * p > segment_start + segment_size:
        break

      first_multiple = max(p * p, ((segment_start + p - 1) // p) * p)
      is_prime_segment[first_multiple - segment_start:segment_size:p] = False

    all_primes.extend(np.nonzero(is_prime_segment[:segment_size])[0] + segment_start)
    segment_start += segment_size
  
  return all_primes

start = 0
stop = 100000000
chunk_size = 65536
primes = segmented_sieve(start, stop, chunk_size)
print(f"Primes in the range [{start}-{stop}]:", primes)