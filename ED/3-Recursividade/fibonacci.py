
def fib_rec(n: int) -> int:
  print(n)
  if n <= 1:
    return n
  else:
    return fib_rec(n-1) + fib_rec(n-2)

print(fib_rec(50))

def fib_ite(n: int) -> int:
  i: int = 1
  fib: int = 1
  anterior: int = 0
  while i < n:
    temp = fib
    fib = fib + anterior
    anterior = temp
    i += 1
  return fib

#print(fib_ite(100))