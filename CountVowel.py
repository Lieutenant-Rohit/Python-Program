def countVowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count+=1
    return count

input_Text = input("Enter a String:- ")
print(f"Number of Vowel present in \"{input_Text}\" is {countVowels(input_Text)}")