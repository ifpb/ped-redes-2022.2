def imprimir_numero_recursivo(num: int):
  if num < 5:
    imprimir_numero_recursivo(num + 1)
    print(num)

def soma(m: int, n: int) -> int:
  if m == n:
    return m
  else:
    return m+soma(m+1, n)

## soma(1,5) = 1 + 14
## soma(2,5) = 2 + 12
## soma(3,5) = 3 + 9
## soma(4,5) = 4 + 5
## soma(5,5) = 5


    
print(soma(1,5))