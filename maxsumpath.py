'''You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers. For example, [[1], [2, 3], [1, 5, 1]] represents the triangle: We define a path in the triangle to start at the top and go down one row at a time to an adjacent value, eventually ending with an entry on the bottom row. For example, 1 -> 3 -> 5. The weight of the path is the sum of the entries. 
Problem #672'''

def goodpairing(l,m):
  result = []
  for i in range(len(l)):
    if m[i] < m[i+1]:
      result.append(l[i]+m[i+1])
    else:
      result.append(l[i]+m[i])
  return result

def maxsumpath(l):
  m = len(l)
  result = goodpairing(l[-2],l[-1])
  
  for i in range(m-3,-1,-1):
    result = goodpairing(l[i],result)
  return result[0]
