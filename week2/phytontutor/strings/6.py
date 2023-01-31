s = input()
if s.find('f') == -1:
    print(-2)
else:
    if s.count('f') == 1:
        print(-1)
    else:
        a = s.find('f') + 1
        print(s.find('f', a , len(s))) 