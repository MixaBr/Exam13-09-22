def is_palindrome(word):
    word.islower()
    if word == word[::-1]:
        return True
    return False

print(is_palindrome("summer"))
print(is_palindrome("шалаш"))