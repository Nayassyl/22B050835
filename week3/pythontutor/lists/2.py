st = input()
parts = st.split(" ")
numbers = [int(i) for i in parts]
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        print(numbers[i])