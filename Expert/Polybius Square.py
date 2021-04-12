# The Polybius Square cipher is a simple substitution cipher that makes use of a 5x5 square grid. The letters A-Z are written into the grid, with "I" and "J" typically sharing a slot (as there are 26 letters and only 25 slots).
# 	1	2	3	4	5
# 1	A	B	C	D	E
# 2	F	G	H	I/J	K
# 3	L	M	N	O	P
# 4	Q	R	S	T	U
# 5	V	W	X	Y	Z

# To encipher a message, each letter is merely replaced by its row and column numbers in the grid.

# Create a function that takes a plaintext or ciphertext message, and returns the corresponding ciphertext or plaintext.

# https://edabit.com/challenge/2C3gtb4treAFyWJMg

def find_cipher(l):
    cipher=[['A', 'B', 'C', 'D', 'E'], ['F', 'G', 'H', 'IJ', 'K'], ['L', 'M', 'N', 'O', 'P'], ['Q', 'R', 'S', 'T', 'U'], ['V', 'W', 'X', 'Y', 'Z']]
    if l.isdigit():
        l=int(l)
        return cipher[l[0]][l[1]]
    else:
        l=l.upper()
        for r in cipher:
            for c in r:
                return str(cipher.index(r)) + str(c.index(l[1]))
                    
def polybius(l):
    cipher=''
    for i in str(l):
        cipher+=find_cipher(i)
    return cipher

print(polybius(2324))