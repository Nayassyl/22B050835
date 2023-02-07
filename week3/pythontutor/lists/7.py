st = input()
h = int(input())
parts = st.split(" ")
numbers = [int(i) for i in parts]
for i in range(len(numbers)):
    if numbers[i] < h:
        print(i + 1)
        break
    elif numbers[len(numbers) - 1] >= h:
        print( len(numbers) + 1 )
        break