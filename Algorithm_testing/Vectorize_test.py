import numpy as np


def fun(a):
    if a == 1:
        return 85
    elif a == 2:
        return 170
    elif a == 3:
        return 255
    return 0


mas = np.array([[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]])
vfun = np.vectorize(fun)
res = vfun(mas)
print(res)
