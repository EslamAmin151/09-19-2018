word = (input("Enter your word: "))
def palindromes(x):
    reversed_word =""
    for index in range(len(word)-1,-1,-1):
        reversed_word += word[index]
    print (reversed_word)
    if word ==  reversed_word:
        return True
    else:
        return False

isPalindrome = palindromes("x")
if isPalindrome == True:
    print (word + " is a palindrome ")
else:
    print (word + " is not a palindrome ")
