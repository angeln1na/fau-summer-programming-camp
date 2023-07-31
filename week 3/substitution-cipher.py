#1. import the string library

#2. import the random library

char = "" + string.digits + string.ascii_letters
#3. create variable for char and set it equal to list then place open and close paranetheses and have char passed inside

#4. create a variable w set it equal to char.copy and then place open and close parentheses next to it

random.shuffle(w)

#5. create an input variable for plain_accountName that says "Please enter the account name: "

#6. create an input variable for plain_accountPassword that says "Please enter your password: "

#7. create a variable cipher_Atext and set it equal to ""

#8. create a variable cipher_Ptext and set it equal to ""

#9. Write a for loop for letter in plain_accountName

  index = char.index(letter)
  cipher_Atext += w[index]

#10. Write a for loop for letter2 in plain_accountPassword
  index = char.index(letter2)
  cipher_Ptext += w[index]
print(f"Ciphered account Name: {cipher_Atext}")
print(f"Ciphered password: {cipher_Ptext}")

# Decryption

#11. create a variable decipher_Atext and set it equal to ""

#12. create a variable decipher_Ptext and set it equal to ""

#13. Write a for loop for letting in cipher_Atext

  index = w.index(letter)
  decipher_Atext += char[index]

#14. Write a for loop for letter2 in cipher_Ptext

  #15. set index = to w.index and pass letter2 in open and closed parentheses
  decipher_Ptext += char[index]

print(f"Deiphered account Name: {decipher_Atext}")
print(f"Deiphered password: {decipher_Ptext}")

