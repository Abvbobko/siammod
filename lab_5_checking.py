import numpy as np

lmbd = 4
u1 = 2
u2 = 2
p = 0.6

a = np.array([
#     000  002 010 012  211 111 110 212
    [-lmbd, u2, u1, 0, 0, 0, 0, 0],
    [lmbd*(1-p), -(u2+lmbd), 0, u1, u2, 0, 0, 0],
    [lmbd*p, 0, -(u1+lmbd), u2, 0, 0, u1, 0],
    [0, lmbd*p, lmbd*(1-p), -(u1+u2+lmbd), 0, u1, 0, u2],
    [0, lmbd*(1-p), 0, 0, -(u2+lmbd*p), 0, 0, u1],
    [0, 0, 0, lmbd*p, 0, -(u1+u2), lmbd*(1-p), lmbd*p],
    [0, 0, lmbd*p, 0, 0, u2, -(lmbd*(1-p) + u1), 0],
    # [0, 0, 0, lmbd*(1-p), lmbd*p, 0, 0, -(lmbd*p+u1+u2)]
    [1, 1, 1, 1, 1, 1, 1, 1]
])
b = np.array([0, 0, 0, 0, 0, 0, 0, 1])
x = np.linalg.solve(a, b)
p000, p002, p010, p012, p211, p111, p110, p212 = x
labels = "p000, p002, p010, p012, p211, p111, p110, p212".split(', ')
# print("p000, p002, p010, p012, p211, p111, p110, p212")
# print(x)
for (k, v) in zip(labels, x):
    print(f'{k}: {v}')
