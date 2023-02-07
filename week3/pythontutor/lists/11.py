st = input()
k = int(input())
parts = st.split(" ")
numbers = [int(i) for i in parts]
for i in range(len(numbers)):
    if i == k: del numbers[k]
for i in range(len(numbers)):
    print(numbers[i])