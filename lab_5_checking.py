import numpy as np

lmbd = 4
u1 = 2
u2 = 2
p = 0.6

a = np.array([
#     000  002 010 012  201 111 110 212
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
p000, p002, p010, p012, p202, p112, p110, p212 = x
labels = "p000, p002, p010, p012, p211, p111, p110, p212".split(', ')
# print("p000, p002, p010, p012, p211, p111, p110, p212")
# print(x)

a1 = (p110 + p010 + p112 + p012 + p212)*u1
q1 = a1/(lmbd*p)
print(1-q1)

# p_otk1 = (p112+p110)#*lmbd*p
# print(p_otk1)

a2 = (p002 + p012 + p202 + p112 + p212)*u2
q2 = a2/(lmbd*(1-p))
print(1-q2)

# p_otk2 = (p212+p202+p112)
# p_otk2 = p_otk2 + (1-p_otk2)*((p212+p202)/(p002+p012+p202+p112+p212))*(lmbd*p)/(lmbd*p + u1)
# print(p_otk2)

for (k, v) in zip(labels, x):
    print(f'{k}: {v}')


# potk1: 0.39560439560439564
# potk2: 0.3697425488017294
# p000: 0.12601207593620342
# p002: 0.09207787659987965
# p010: 0.1599462752725272
# p012: 0.1187886468614845
# p211: 0.05663532218919168
# p111: 0.18576870777174267
# p110: 0.20983568783265294
# p212: 0.050935407536318
