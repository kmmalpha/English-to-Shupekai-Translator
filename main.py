translations = {
    "b": "ba",
    "c": "chi",
    "d": "di",
    "f": "fu",
    "g": "ga",
    "h": "ha",
    "j": "gi",
    "k": "kai",
    "l": "la",
    "m": "mu",
    "n": "ne",
    "p": "pe",
    "q": "ki",
    "r": "ro",
    "s": "shu",
    "t": "ta",
    "u": "'",
    "v": "we",
    "w": "wu",
    "x": "zo",
    "y": "yo",
    "z": "zi",
}


def translate(word):
    translation = ""
    for letter in word:
        if letter.lower() in translations.keys():
            if letter.islower():
                translation += translations.get(letter)
            else:
                translation += translations.get(letter.lower()).capitalize()
        else:
            translation += letter
    return translation


print(translate(input("Enter a phrase: ")))

# the quick brown fox jumps over the lazy dog.
# The Quick Brown Fox Jumps Over The Lazy Dog.
# THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG!
