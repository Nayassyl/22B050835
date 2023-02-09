def is_palindrome(str):
    for i in range(len(str)):
        if str[ len(str) - 1 - i] == str[i]:
            return True
    return False
s = input()
print(is_palindrome(s))