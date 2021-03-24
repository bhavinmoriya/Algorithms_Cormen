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
