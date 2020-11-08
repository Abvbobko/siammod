p1 = 0.7
print(1/(1-p1))
print("queue (1): ", 2/(1-p1))
print("queue (2): ", 3/(1-p1))

result = 0
for i in range(1000):
    result += i*(1-p1)*p1**(i-1)
print(result)