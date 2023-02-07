st = input()
parts = st.split(" ")
numbers = [int(i) for i in parts]
for i in range(len(numbers) - 1 ):
    if i % 2 == 0:
        a = numbers[i + 1]
        numbers[i+1] = numbers[i]
        numbers[i] = a
for i in range(len(numbers)):
    print( numbers[i])