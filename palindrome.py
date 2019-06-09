words = input("Enter some text please ")
letters = "abcdefghijklmnopqrstuvwxyz"
words = words.lower()
og = []
new = []
count = 0

def addLetters(place):
    if place < len(words):
        if words[place] in letters:
            og.append(words[place])
            new.insert(0, words[place])
        place += 1
        addLetters(place)

addLetters(count)



if og == new:
    print(words + " is a palidrome!")
else:
    print(words + " is not a palidrome.")
