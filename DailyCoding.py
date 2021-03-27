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

'''Given a list of points, a central point, and an integer k, find the nearest k points from the central point.

For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central point (1, 2), and k = 2, return [(0, 0), (3, 1)].'''
def distance(a,b):
  return (a[0]-b[0])**2 + (a[1]-b[1])**2
def closestpnts(l,k,center):
  dist = {}
  for i in range(len(l)):
    dist[l[i]] = distance(l[i],center)
  b = list(dist.values());
  b1 = set(b)
  b = list(b1); b.sort()
  print(b)
  c = []
  for i in range(k):
    if len(c) < k+1:
      for key in dist.keys():

        if dist[key] == b[i] and len(c) < k+1:
          c.append(key)

  if len(c) > k:
    c = c[0:k]
  return c

'''This problem was asked by Square.

Given a list of words, return the shortest unique prefix of each word. For example, given the list:

dog
cat
apple
apricot
fish
Return the list:

d
c
app
apr
f

Problem #680 '''

def getLeastPrefix(l):
  m = len(l)
  prefix = [l[i][0] for i in range(m)]
  s = set(prefix)
  while len(s) != m:
    for i in range(m):
      for j in range(i+1,m):
        while prefix[i] == prefix[j]:
          a = len(prefix[i])
          prefix[i] = l[i][0:a+1]
          prefix[j] = l[j][0:a+1]
    s = set(prefix)
  return prefix


