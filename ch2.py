# Insert sort
def insert_sort(l):
  m = len(l)
  if m == 1:
    return l
  else:
    for j in range(1,m):
      key = l[j]
      i = j-1
      while i >= 0 and l[i] > key:
        l[i+1] = l[i]
        i = i-1
      l[i+1] = key
    return l 

# Pop sort for decreasing order
def pop_sort(l):
  m = len(l)
  for i in range(m):
    for j in range(i+1,m):
      if l[i] < l[j]:
        l[i], l[j] = l[j], l[i]
  return l

'''Write pseudocode for linear search, which scans through the sequence, looking
        for value v. Using a loop invariant, prove that your algorithm is correct.'''

def search_prob(l,v):
  m = len(l)
    for i in range(m):
        if l[i] == v:
            return i
    return print("NIL")

# Sum of two binary arrays
def binary_sum(a,b):
  n = len(a)
  c = []
  for i in range(n):
    if a[n-i-1]+b[n-i-1] == 1:
      c.append(1)
    elif a[n-i-1]+b[n-i-1] == 2:
      c.append(0)
      a[i] += 1
    elif a[n-i-1]+b[n-i-1] == 3:
      c.append(1)
      a[i] += 1
    else:
      c.append(0)
  c.append(1)
  c.reverse()
  return c

#Horner’s rule
def poly_eval(coeff,x):
  y = 0
  n = len(coeff)
  for i in range(n):
    y = coeff[n-i-1] + x*y 
  return y 

# Find number of inversions
def num_inversion(l):
  inv =[]
  for i in range(len(l)-1):
    for j in range(i+1,len(l)):
      if l[i] > l[j]:
        inv.append([l[i],l[j],(i,j)])
  return [inv, len(inv)]

