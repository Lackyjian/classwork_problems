l1 = ['m', 'n']
l2 = []
n = 3
for x in range(len(l1)):
    for i in range(n):
        a = l1[x]+str(i+1)
        l2.append(a)
print(l2)