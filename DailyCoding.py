'''Given a positive integer n, find the smallest number of squared integers which sum to n.'''

def getMinSquares(n):
  import math
  if n<=3:
    return n
  elif math.sqrt(n)%1 == 0:
    return 1
  else:
    k = 1
    result = n
    while k*k <=n:
      result = min(result, 1+getMinSquares(n-k*k))
      k += 1
    return result
