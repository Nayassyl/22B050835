def unique(list):
    x = []
    for i in range(len(list)):
        if list.count(list[i]) == 1:
            x.append(list[i])
    return(x)

a = [s for s in input().split()]
print(unique(a))