s = input()
n = int(input())
m = int(input())
s3 = s[n: m + 1]
print(s[:n] + s3[::-1] + s[m+1:])