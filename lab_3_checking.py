import numpy as np

r = 0.1
p1 = 0.7
p2 = 0.5

print(
    r*p1*p2 + (1-r)*((1-p1)*p2 + (1-p2)*p1),
    (1-r)*p1*p2,
    r*((1-p1)*p2 + (1-p2)*p1) + (1-r)*(1-p1)*(1-p2)
)

a = np.array([
#     000  001   010   011  111 211
    [-0.9, 0.05, 0.03, 0.015, 0, 0],
    [0, -0.95, 0, 0.015, 0, 0],
    [0.9, 0.45, -0.66, 0.17, 0.015, 0],
    [0, 0.45, 0.63, -0.515, 0.185, 0.015],
    [0, 0, 0, 0.315, -0.515, 0.185],
    # [0, 0, 0, 0, 0.315, -0.2],
    [1, 1, 1, 1, 1, 1]
])
b = np.array([0, 0, 0, 0, 0, 1])
x = np.linalg.solve(a, b)
p000, p001, p010, p011, p111, p211 = x
print("p000, p001, p010, p011, p111, p211")
print(x)
# print(x)
# print(p000, p001, p010, p011, p111, p211)
# print(np.allclose(np.dot(a, x), b))
A = (1-p1)*p010 + (1-p2)*p001 + (p2*(1-p1) + p1*(1-p2) + 2*(1-p1)*(1-p2))*(p011+p111+p211)
print("A", A)

lmbd = 0.9
Q = A/lmbd
print("Q:", Q)
print("Pотк:", 1-Q)
L_queue = 1*p111 + 2*p211
print("L_queue: ", L_queue)

L_system = 1*p010 + 1*p001 + 2*p011 + 3*p111 + 4*p211
print("L_system: ", L_system)

W_queue = L_queue/A
W_system = L_system/A
print("W_queue:", W_queue)
print("W_system:", W_system)

K1 = p010 + p011 + p111 + p211
K2 = p001 + p011 + p111 + p211
print("K1:", K1)
print("K2:", K2)

# A: 0.75971
# lambda: 0.89944
# Q: 0.8603000000000001
# Pотк: 0.1397
# Lоч: 1.17358
# Lc: 3.09298
# Wоч: 1.5447736636348082
# Wс: 4.071185057456135
# K_кан1: 0.99096
# K_кан2: 0.92844
