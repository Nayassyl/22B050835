def even_numbers(n):
    for i in range(1, n):
        if i % 2 == 0:
            yield i
for x in even_numbers(int(input())):
    print(x, end = ", ")