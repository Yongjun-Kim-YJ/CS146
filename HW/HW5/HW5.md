## Problem 1

1. T(N) = 2T(N-1) + 1
- Recursion tree
- Height of the tree is N.
- At each level(i), there are (2^i) nodes, and each node performs a constant amount of work.
- Therefore, the total time complexity is:
  T(N) = O(2^N)

2. T(N) = 3T(N-1) + n
- T(N) = aT(N/b) + f(N)
  where a = 3, b = 1, and f(N) = n.
  n = O(1^N) = O(1)
- Therefore, Case 2 of the master method:
  T(N) = O(nlog n)

3. T(N) = 9T(N/2) + n^2
- T(N) = aT(N/b) + f(N)
  where a = 9, b = 2, and f(N) = n^2.
  c = log_2(9)
  n^2 = O(n^{log_b(a)}) = O(n^{log_2(9)})
- Therefore, Case 2 of the master method:
  T(N) = O(n^{log_2(9)})

4. T(N) = 100T(N/2) + n^{log_2(c) + 1} (where c is a constant)
- T(N) = aT(N/b) + f(N)
  where a = 100, b = 2, and f(N) = n^{log_2(c) + 1}.
  f(N) = n^{log_2(c) + 1} = n^{log_2(100) + 1} = n^{6.64 + 1} = n^{7.64}
- Therefore, Case 1 of the master method:
  T(N) = O(f(N)) = O(n^{7.64})

5. T(N) = 4T(N/2) + n^2*(log n)
- T(N) = aT(N/b) + f(N)
  where a = 4, b = 2, and f(N) = n^2*(log n).
  n^2*(log n) = O(n^2*(log n))
- Therefore, Case 2 of the master method:
  T(N) = O(n^2*(log n))

6. T(N) = 5T(N/2) + n^2/\log n
- T(N) = aT(N/b) + f(N)
  where a = 5, b = 2, and f(N) = n^2/log n.
  n^2/log n = O(n^{log_b(a) - e}) = O(n^{2.32 - e})
- Therefore, Case 3 of the master method:
  T(N) = O(n^{log_2(5)})

## Problem 2

T(n)=2T(n/2)+O(n)

T(n)=aT(n/b)+f(n)
where a=2, b=2, and f(n)=10n

f(n)=O(n^(log_b(a)))=O(n^(log_2(2)))=O(n)

Case 2,

T(n) = O(nlog n)