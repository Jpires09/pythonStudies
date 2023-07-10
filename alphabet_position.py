from operator import indexOf


def alphabet_position(text):
    ALPHABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    reversed = []
    for letter in text:
        for element in ALPHABET:
            if (letter == element or letter == element.lower):
                reversed.append(indexOf(element))


    return reversed.join(" ")