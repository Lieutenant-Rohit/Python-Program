def checkPalindrome(text):
    if text == text[::-1]:
        return "Palindrome"
    else:
        return "Not a Palindrome"

text = input("Enter a String:- ")
print(checkPalindrome(text))