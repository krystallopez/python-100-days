# Caesar cipher project for Day 8 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # duplicated letters to avoid getting index error as if you enter a word that has a z in it, once the loop gets to z the index will then be out of range and we would need to start from the beginning of the list again 

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n") # This was the user is going to type in
text = input("Type your message:\n").lower() # This input will be stored in the text variable and passed as a parameter in the function
shift = int(input("Type the shift number:\n")) # This input will be stored in the text variable and passed as a parameter in the function


def encrypt(plain_text, shift_amount):
  cipher_text = "" 
  # This will represent the new encoded word
  for letter in plain_text: 
  # This will go through each letter in the plain_text value
    
    position = alphabet.index(letter) 
    
    # This will give us the index of the letter that we get from looping through the plain_text variable. Once we have that, we save the index of that letter into the variable called position, which notes the position of the letter in the alphabet list. 
    
    new_position = position + shift_amount 
    
    # This is equal to the previous position plus the shift amount. For example if the letter is h, the letter 'h' has an index of 7 in the alphabet list. we would add 7 to 5, which is 12 which encodes the letter h to be the 12th index of the alphabet list, which would be the letter 'm. This would follow suit for each letter in plain_text. 
    
    new_letter = alphabet[new_position] 
    
    # This is showing that for each letter, the new letter for the encrypted password is equal to the alphabet at the index of the new_position which is a number
    
    cipher_text += new_letter 
    
    # For each letter in the plain_text that is made into the new_letter; each new_letter will be added into cipher_text to create the new encoded password
  print(f"The encoded text is {cipher_text}") 

def decrypt(cipher_text, shift_amount):
  plain_text = ""
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    plain_text += alphabet[new_position]
  print(f"The decoded text is {plain_text}")

# This is the same process as for the encrypt except we are subtracting the shift_amount and changing the empty string variable to plain text.

# This conditional will check to see of the user wants to decrypt or encrypt a word based on whether or not they type in "encode" or "decode". If the user types in "encode", then the word they entered will be encrypted, if the user types in "decode" then the word they entered in will be decrypted

if direction == "encode":
  encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
  decrypt(cipher_text=text, shift_amount=shift)


#-----------------------------------------------------------------------------
# Instructions- Encryption
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#e.g. 
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"

##HINT: How do you get the index of an item in a list:
#https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

#Instructions- Decryption
#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.