# was not sure how to write the if-comparison
# found from the following YouTube video as reference : https://www.youtube.com/watch?v=-9degjR16bY

def palindrome(word):
    mid = len(word) // 2

    for i in range(0, mid):
        if word[i] == word[len(word) - i - 1]:  # reference
            return f"Your word is a palindrome"
        else:
            return f"Your word is not a palindrome"


user_input = input("Enter a word: ")
print(palindrome(user_input))