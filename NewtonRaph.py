import numpy as np


f = lambda x: np.e**(-x) - x
fp = lambda x: -1*(np.e**(-x))-1
iters = 15

x = np.linspace(-5, 5, 11)
tb = [(x[i], f(x[i])) for i in range(x.size)]

print('\nTabla:')

for i in tb:
    print(i)

valor_in = np.min(np.abs(f(x)))

print ('\nValor inicial: ', valor_in)

xo = valor_in
for i in range(iters):
    xf = xo - f(xo)/fp(xo)
    print(f'Iter {i+1}/{iters}: {xf}')
    xo = xf