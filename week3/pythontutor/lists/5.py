st = input()
parts = st.split(" ")
cnt = 0
numbers = [int(i) for i in parts]
for i in range(1, len(numbers) - 1):
    if numbers[i] > numbers[i - 1]  and  numbers[i + 1] < numbers[i]:
        cnt += 1
print(cnt)