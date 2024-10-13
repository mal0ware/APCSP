MAX = 1000

a = 1
b = 1
c = 1
print(a)
print(b)
while c < MAX:
        c = a + b
        a = b
        b = c
        if c < MAX:
            print(c)