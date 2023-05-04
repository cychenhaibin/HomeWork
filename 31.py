import numpy as np
a = np.array([[1.,2.],[3.,4.]])
y = np.array([[5.],[7.]])
print(a)
print(a.T)
b=np.eye(2)
print(b)
print(b.trace())
print(np.linalg.solve(a, y))


        