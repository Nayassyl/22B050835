def swap_columns(list, i, j):
    for k in range(len(list)):
        list[k][i] , list[k][j] = list[k][j], list[k][i]
    for row in list:
        for elem in row:
            print(elem,end=' ')
        print()


n , m = [int(s) for s in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
val_i, val_j =[int(s) for s in input().split()]
swap_columns(a, val_i, val_j)
