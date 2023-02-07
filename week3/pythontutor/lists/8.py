st = input()
cnt = 1
parts = st.split(" ")
numbers = [int(i) for i in parts]
for i in range(len(numbers) - 1):
    if numbers[i] != numbers[i+1]:
        cnt += 1
print(cnt)