def encrypt_password(password):
  #1. Write the variable encrypted_password and set it equal to ""

  #2. Write a for loop for char in password
    if char.isalpha():
      #3. Write the variable ascii_val and set it equal to ord(char)

      shifted_val = (ascii_val - 97 + 3) % 26 + 97

      #4. Write the variable encrypted_password set it plus and equal to chr open and close parentheses with shifted_val inside
    
    #5. Write an else statement starting with else
      
      #6. Write the variable encrypted_password and set it to plus and equal to char
      
  #7. Write return and the variable used in number 6

def decrypt_password(password):

  #8. Write the variable decrypted_password and set it equal to ""

  #9. Write a for loop for char in password

    if char.isalpha():
      ascii_val = ord(char)
      shifted_val = (ascii_val - 97 - 3) % 26 + 97
      decrypted_password += chr(shifted_val)
    #10. Write an else statement starting with else

      #11. Write the variable decrypted_password and set it to plus and equal to char
  # 12. Write return and the variable used in number 11

def main():
  #13. Create an input variable password that says "Please enter a password"

  #14. Write a print statement that says "Please choose the following options"

  #15. Write a print statement that says "1 = Encrypt the password"

  #16. Write a print statement that says "2 = Decrypt the password"

  choice - int(input())

  if choice == 1:
    encrypted_password = encrypt_password(password.lower())
    print("Encrypted Password", encrypted_password)
  elif choice == 2:
    decrypted_password = decrypt_password(password.lower())
    print("Decrypted Password:", decrypted_password)
  else:
    print("Error: Invalid choice")

if __name__ == "__main__":
  main()
