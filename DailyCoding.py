'''Given a positive integer n, find the smallest number of squared integers which sum to n.
Daily Coding Problem: Problem #670'''

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

'''This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?'''

def twoSum(l,k):
  #l.sort()
  for i in range(len(l)):
    j = 0
    while j != i and j < len(l):
      if l[j]+l[i] == k:
        return True
        #break
      else:
        j += 1
  return False

''' Get the minimal path '''

def minpairing(l,m):
  result = []
  for i in range(len(l)):
    if m[i] < m[i+1]:
      result.append(l[i]+m[i])
    else:
      result.append(l[i]+m[i+1])
  return result

def minsumpath(l):
  m = len(l)
  result = minpairing(l[-2],l[-1])

  for i in range(m-3,-1,-1):
    result = minpairing(l[i],result)
  return result[0]

  '''The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N. The method is to take increasingly larger prime numbers, and mark their multiples as composite.

For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two), then [6, 9, 12, ...] (multiples of three), and so on. Once we have done this for all primes less than N, the unmarked numbers that remain will be prime.

Implement this algorithm.

Bonus: Create a generator that produces primes indefinitely (that is, without taking N as an input).

Daily Coding Problem: Problem #677 '''

N = int(input("Give me number N until which you want to list primes"))
l = [i for i in range(N+1)]
import math
k = int(math.sqrt(N))
for i in range(2,k+1):
  j=2
  while i*j <= N:
    l[i*j]=0
    j += 1
while 0 in l:
  l.remove(0)
l.remove(1)
print(l)
