## Problem 1:

1. 10000000000n^2 vs n^3

- 10000000000n^2: This is a quadratic function.
- n^3: This is a cubic function.

As n approaches infinity, the cubic function grows faster than the quadratic function.
Therefore, n^3 is asymptotically greater than 10000000000n^2.

2. n^2 log(n) vs n(log(n))^10

- n^2 log(n): This function grows faster than n log(n) because of the quadratic term.
- n(log(n))^10: This function grows slower than n^2 log(n) because the logarithmic term is raised to a constant power.

As n approaches infinity, the function with the quadratic term and a logarithmic term grows faster than the function with a linear term and a logarithmic term raised to a constant power.
Therefore, n^2 log(n) is asymptotically greater than n(log(n))^10.

3. n^(log(n)) vs 2^(sqrt(n))

- n^(log(n)): This function grows exponentially because log(n) grows very slowly compared to n.
- 2^(sqrt(n)): This function also grows exponentially but at a slower rate compared to n^(log(n)).

As n approaches infinity, the function n^(log(n)) grows much faster than 2^(sqrt(n)).
Therefore, n^(log(n)) is asymptotically greater than 2^(sqrt(n)).

4. 2^n vs 22^n

- 2^n: This is an exponential function with base 2.
- 22^n: This is an exponential function with base 22.

As n approaches infinity, the exponential function with a higher base grows faster.
Therefore, 22^n is asymptotically greater than 2^n.

## Problem 2:
1. Best Case:
   - The best case occurs when `n` is divisible by a small number early in the loop.
   - This would happen when `n` is even and `i = 2`, resulting in O(1) time complexity.

2. Worst Case:
   - The worst case occurs when `n` is a prime number.
   - The loop runs from 2 to sqrt(n), as `i*i <= n` is equivalent to `i <= sqrt(n)`.
   - The number of iterations in the worst case is approximately sqrt(n).
   - Therefore, the time complexity is O(sqrt(n)).

3. Average Case:
   - The average case time complexity is similar to the worst case because, on average, we may need to check up to sqrt(n) to determine if `n` is a prime number.
   - Therefore, the average case time complexity is O(sqrt(n)).

- Best Case: O(1)
- Worst Case: O(sqrt(n))
- Average Case: O(sqrt(n))