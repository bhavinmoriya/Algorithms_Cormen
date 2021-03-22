def merge(a,b):
    c = []
    m = len(a)
    n = len(b)
    while m > 0 and n > 0:
      if a[0] > b[0]:
        c.append(b[0])
        b.remove(b[0])
        n -= 1
      else:
        c.append(a[0])
        a.remove(a[0])
        m -= 1
    while m > 0:
      return c + a
    while n > 0:
      return c + b
def mergesort(l):
  m = len(l)
  if m == 1:
    return l
  else:
    a = mergesort(l[0:int(m/2)])
    b = mergesort(l[int(m/2):m])
  return merge(a,b)
