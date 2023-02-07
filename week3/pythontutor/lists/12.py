st = input()
k = input()

parts = st.split(" ")
numbers = [int(i) for i in parts]
numbers.insert( k[:k.find(" ")] ,int( k[(k.find(" ") + 1):]))
for i in range(len(numbers)):
    print(numbers[i])