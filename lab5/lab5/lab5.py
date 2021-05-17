class Matrix_input(object):
    

    def Matrix_len(n,a):
       for i in range(n):
           for j in range(n):
               a[j].append(a[i][j])
       for k in range(n):
           for i in range(n):
               a[i].pop(0)
       Transposition.Trans(a)


class Transposition(object):

    def Trans(a):
        for i in range(len(a)):
            print(*a[i])

def main():
    x = int(input("Введите розмер: "))
    y =[list(map(int, input("Введите строку: ").split())) for i in range(x)]
    Matrix_input.Matrix_len(x,y)

main()

