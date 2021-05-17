n = int(input("Введите розмер матрици"))
a =[list(map(int, input("Введите строку:").split())) for i in range(n)]
for i in range(n):
    for j in range(n):
        a[j].append(a[i][j])
for k in range(n):
    for i in range(n):
        a[i].pop(0)
print("\n")
for i in range(len(a)):
    print(*a[i])