st = input()
if len(st) == 1:
    print(st)
else:
    parts = st.split(" ")
    numbers = [int(i) for i in parts]
    maxx =  -1000000000
    minn = 1000000000
    for i in range(0, len(numbers)):
        if numbers[i] > maxx:
            maxx = numbers[i]
            maxind = i
    for i in range(0, len(numbers)):
        if numbers[i] < minn:
            minn = numbers[i]
            minind = i
    
    numbers[maxind] = minn
    numbers[minind] = maxx
    for i in range(len(numbers)):
        print( numbers[i], end = ' ')