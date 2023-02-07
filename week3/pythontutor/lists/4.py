st = input()
parts = st.split(" ")
numbers = [int(i) for i in parts]
for i in range(len(numbers) - 1):
    if numbers[i] > 0 and  numbers[i + 1] > 0:
        print( numbers[i] , numbers[i + 1])
        break
    elif numbers[i] < 0 and  numbers[i + 1] < 0:
        print( numbers[i] , numbers[i + 1])
        break