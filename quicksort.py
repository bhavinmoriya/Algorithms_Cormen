def arrange(l):
    m = len(l)
    hi = 0
    lo = m-2
    while l[hi] < l[-1]:
        hi += 1 
    if hi == m-1:
        return l, hi, lo # will return l with l[-1] as the largest
    while l[lo] > l[-1]:
        lo -= 1
    return l, hi, lo   

def quicksort(l):
  m = len(l)
  if m == 1 or m == 0:
      return l
  elif m == 2:
      if l[0] <= l[1]:
          return l
      else:
          return l.reverse()
      
  pivot = int(m/2)
  l[-1], l[pivot] = l[pivot], l[-1]
  
  l, hi, lo = arrange(l) 
  
  while hi < lo:
    l[hi], l[lo] = l[lo], l[hi]
    l, hi, lo = arrange(l)
  l[hi], l[-1] = l[-1], l[hi]
  a = quicksort(l[0:hi])
  b = quicksort(l[hi+1:])  
  return a+l[hi:hi+1]+b
  
a=[7, 5, 1]
quicksort(a)
