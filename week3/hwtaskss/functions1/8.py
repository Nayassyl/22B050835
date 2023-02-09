def has_007_order(list):
    c = False
    for i in range(0, len(list)):
        if list[i] == 0:
            for j in range(i + 1, len(list)):
                if list[j] == 0:
                    for k in range(j + 1, len(list)):
                        if list[k] == 7:
                            c = True
                            break
    return c
        


a = [int(s) for s in input().split()]
print(has_007_order(a))