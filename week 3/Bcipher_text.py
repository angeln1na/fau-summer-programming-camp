
#subsutation cipher
import string 
import random

char = "" + string.digits + string.ascii_letters
char = list(char)
w = char.copy()
random.shuffle(w)

plain_accountName = input("[please enter the account name pls and ty!")
plain_accountPassword = input("pelase enter your password")

cipher_Atext = ""
cipher_Ptext = ""

for letter in plain_accountName:
    index = char.index(letter)
    cipher_Atext += w[index]

for letter2 in plain_accountPassword:
    index = char.index(letter2)
    cipher_Ptext += w[index]


print(f"cipher account Name: {cipher_Atext}")
print(f"cipher password Name: {cipher_Ptext}")

# add the decreyption part 


