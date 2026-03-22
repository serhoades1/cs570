import random
sentence = "This is a sentence"

def shuffleSentence(s):
    newSentence = ""
    words = s.split()
    for i in range(len(words)):
        words[i] = words[i] + str(i)
    random.shuffle(words)
    for i in range(len(words)):
        if i + 1 > len(words):
            newSentence = newSentence + words[i]
            break
        newSentence = newSentence + words[i] + " "
    return newSentence

def unshuffleSentence(s):
    words = s.split()
    reversedWords = [word[::-1] for word in words]
    sorted(reversedWords)
    words = [word[::-1] for word in reversedWords]
    newSentence = ""
    for i in range(len(words)):
        if i + 1 > len(words):
            newSentence = newSentence + words[i]
            break
        newSentence = newSentence + words[i] + " "
    return newSentence

print(shuffleSentence(sentence))
print(unshuffleSentence(sentence))