#ELIMINACION GAUSSIANA PYTHON JUANMA
from numpy import array, zeros, fabs, linalg

a = array([[0, 6, -1, 2, 2],
           [0, 3, 4, 1, 7],
           [5, 1, 0, 3, -1],
           [3, 1, 3, 0, 2],
           [4, 4, 1, -2, 1]], float)
# los términos constantes de la matriz b de las ecuaciones
b = array([5, 7, 2, 3, 4], float)

print("Solucion de numpy:")


print(linalg.solve(a, b))

n = len(b)
x = zeros(n, float)

# primer bucle especifica la fila fija
for k in range(n-1):
    if fabs(a[k, k]) < 1.0e-12:

        for i in range(k+1, n):
            if fabs(a[i, k]) > fabs(a[k, k]):
                a[[k, i]] = a[[i, k]]
                b[[k, i]] = b[[i, k]]
                break

 # aplica la eliminación debajo de la fila fija

    for i in range(k+1, n):
        if a[i, k] == 0:
            continue

        factor = a[k, k]/a[i, k]
        for j in range(k, n):
            a[i, j] = a[k, j] - a[i, j]*factor
            # también calculamos el vector b de cada fila
        b[i] = b[k] - b[i]*factor
print(a)
print(b)


x[n-1] = b[n-1] / a[n-1, n-1]
for i in range(n-2, -1, -1):
    sum_ax = 0

    for j in range(i+1, n):
        sum_ax += a[i, j] * x[j]

    x[i] = (b[i] - sum_ax) / a[i, i]

print("La solución del sistema es:")
print(x)
