def to_string(list):
    return ''.join(list)

def permutation(a, start, end):
    if start == end:
        print(to_string(a))
    else:
        for i in range (start, end):
            a[start], a[i] = a[i] , a[start]
            permutation(a, start + 1 , end)
            a[start], a[i] = a[i] , a[start]

        

s = input()
l = list(s)
permutation(l, 0, len(s))