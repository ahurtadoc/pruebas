import re


def subword(test, password):
    word = ''
    for i in range(len(test)):
        pattern = word + test[i]
        if (re.search(pattern, password[0])) and (re.search(pattern, password[1])):
            word = pattern
        else:
            break
    return word


def get_password(min_word, password_list):
    correct = ''
    for i in range(len(min_word)):
        res = subword(min_word[i:], password_list)
        if len(correct) < len(res):
            correct = res

    return correct


list = []
words = input().split()

for i in range(3):
    list += [input()]
    words[i] = int(words[i])
minIndex = words.index(min(words))
minWord = list.pop(minIndex)

print(get_password(minWord, list))

