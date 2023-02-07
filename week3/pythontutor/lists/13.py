st = input()
parts = st.split(" ")
numbers = [int(i) for i in parts]
cnt = 0
for i in range(len(numbers)):
    for j in range (i + 1,len(numbers)):
        if numbers[i] == numbers[j]: cnt += 1
print(cnt)