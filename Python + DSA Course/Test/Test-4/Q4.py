"""
Question 4: Ask a sentence from user. Then ask a integer k from user. Print all the
words which are greater or equal to k.
"""


def wordsLargerK(my_string: str, k: int) -> str:
    words = my_string.split()
    result = [i for i in words if len(i) >= k]
    print(result)
    return " ".join(result)


my_string = input("Enter sentence: ")
k = int(input("Enter k: "))
print(wordsLargerK(my_string, k))


# Solution:
def printWords(sentence, k):
    words = sentence.split()
    for word in words:
        if len(word) >= k:
            print(word, end=" ")


sentence = input("Enter a sentence: ")
k = int(input("Enter an integer k: "))

printWords(sentence, k)
