st = input()
parts = st.split(" ")
numbers = [int(i) for i in parts]
max = numbers[0]
ind = 0
for i in range(len(numbers)):
    if numbers[i] > max:
        max = numbers[i]
        ind = i
print(max , ind)