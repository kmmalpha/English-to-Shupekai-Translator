def translate(word):
    translation = ""
    for letter in word:
        if letter in "B":
            translation += "Ba"
        elif letter in "b":
            translation += "ba"
        elif letter in "C":
            translation += "Chi"
        elif letter in "c":
            translation += "chi"
        elif letter in "D":
            translation += "Di"
        elif letter in "d":
            translation += "di"
        elif letter in "F":
            translation += "Fu"
        elif letter in "f":
            translation += "fu"
        elif letter in "G":
            translation += "Ga"
        elif letter in "g":
            translation += "ga"
        elif letter in "H":
            translation += "Ha"
        elif letter in "h":
            translation += "ha"
        elif letter in "J":
            translation += "Gi"
        elif letter in "j":
            translation += "gi"
        elif letter in "K":
            translation += "Kai"
        elif letter in "k":
            translation += "kai"
        elif letter in "L":
            translation += "La"
        elif letter in "l":
            translation += "la"
        elif letter in "M":
            translation += "Mu"
        elif letter in "m":
            translation += "mu"
        elif letter in "N":
            translation += "Na"
        elif letter in "n":
            translation += "ne"
        elif letter in "P":
            translation += "Pe"
        elif letter in "p":
            translation += "pe"
        elif letter in "Q":
            translation += "Ki"
        elif letter in "q":
            translation += "ki"
        elif letter in "R":
            translation += "Ro"
        elif letter in "r":
            translation += "ro"
        elif letter in "S":
            translation += "Shu"
        elif letter in "s":
            translation += "shu"
        elif letter in "T":
            translation += "Ta"
        elif letter in "t":
            translation += "ta"
        elif letter in "U" and "u":
            translation = "'"
        elif letter in "V":
            translation += "We"
        elif letter in "v":
            translation += "we"
        elif letter in "W":
            translation += "Wu"
        elif letter in "w":
            translation += "wu"
        elif letter in "X":
            translation += "Zo"
        elif letter in "x":
            translation += "zo"
        elif letter in "Y":
            translation += "Yo"
        elif letter in "y":
            translation += "yo"
        elif letter in "Z":
            translation += "Zi"
        elif letter in "z":
            translation += "zi"
        else:
            translation += letter

        return translation

"""    correct_grammar = ""
    for vowels in translation:
        if vowels in "AA":
            correct_grammar += "A-A"
        elif vowels in "aa":
            correct_grammar += "-a"
        elif vowels in "EE":
            correct_grammar += "E-E"
        elif vowels in "ii":
            correct_grammar += "ii"
        else:
            correct_grammar += vowels
    """



vowels = ("a", "e", "i", "o", "u")
word = "Muaata"

for index in range(len(word)):
    if word[index] in vowels and word[index+1] in vowels:






"""def grammar(translation):
    correct_grammar = ""
    for vowels in translation:
        if vowels in "AA":
            correct_grammar += "A-A"
        elif vowels in "aa":
            correct_grammar += "a-a"
        elif vowels in "EE":
            correct_grammar += "E-E"
        elif vowels in "ii":
            correct_grammar += "ii"
        else:
            correct_grammar += vowels
    return correct_grammar
"""


print(translate(input("Enter a phrase: ")))
# the quick brown fox jumps over the lazy dog. The Quick Brown Fox Jumps Over The Lazy Dog. THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.
