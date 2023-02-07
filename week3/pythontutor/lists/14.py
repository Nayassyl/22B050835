st = input()
parts = st.split(" ")
numbers = [int(i) for i in parts]
cnt = 0
for i in range(len(numbers)):
    if numbers.count( numbers[i]) == 1 : print (numbers[i])
        