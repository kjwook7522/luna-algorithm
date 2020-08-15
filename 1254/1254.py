from sys import stdin


def is_palindrome(str,str_len):
    for i in range(str_len // 2):
        if str[i] == str[str_len-1-i]:
            continue
        else:
            return False
    return True


str = stdin.readline().rstrip()
str_len = len(str)
is_p = is_pelindrome(str,str_len)
result = str_len

if is_p:
    print(result)
    exit()
else:
    for i in range(str_len,0,-1):
        if is_palindrome(list(reversed(str)),i):
            result = str_len + (str_len - i)
            print(result)
            break
