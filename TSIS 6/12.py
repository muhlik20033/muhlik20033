def palindrom(s: str):
    left = 0
    right = len(s) - 1
    while right >= left:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print(palindrom(input()))