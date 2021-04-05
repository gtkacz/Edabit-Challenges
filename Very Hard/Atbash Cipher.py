# The Atbash cipher is an encryption method in which each letter of a word is replaced with its "mirror" letter in the alphabet: A <=> Z; B <=> Y; C <=> X; etc.

# Create a function that takes a string and applies the Atbash cipher to it.

# https://edabit.com/challenge/MGALfBAXhXqqdFyqo

def find_mirror(letter):
    try:
        if letter.islower():
            alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        else:
            alphabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        i=alphabet.index(letter)
        return alphabet[::-1][i]
    except:
        return letter

def atbash(string):
    encoded=''
    for l in string:
        encoded+=find_mirror(l)
    return encoded

print(atbash('Christmas is the 25th of December'))