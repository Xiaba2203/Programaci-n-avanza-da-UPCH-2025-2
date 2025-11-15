def sumaLista(a):
    if not a:
        return 0
    return a[0] + sumaLista(a[1:])

def sumaN2(n):
    if n <= 0:
        return 0
    return n + sumaN2(n-2)

def sumaNN(n):
    if n == 0:
        return 0
    return n*n + sumaNN(n-1)

def sumaOnes(n, v=1):
    if n == 0:
        return 0
    return v + sumaOnes(n-1, v*10+1)

print(sumaLista([1,2,3,4]))
print(sumaN2(10))
print(sumaNN(5))
print(sumaOnes(4))
