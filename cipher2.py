
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for letter in start_text:
         position = alphabet.index(letter)
         if cipher_direction == "decode":
            shift_amount *= -1
         new_position = position + shift_amount
         end_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is {end_text}")

    

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)


# To make this code look a bit cleaner, we are going to combine the decrypt and encrypt functions into one function called caesar(). We will get rid of the if conditionals and rework our code bit so that we can get it looking much cleaner.

# First, we are going to create our new function called caesar(). The function will take in 3 parameters: the text, the shift, and the direction. We call the text parameter start_text(since we could be passed the plain_text or the cipher_text). Then we will have shift_amount, and the last one will be called cipher_direction to differentiate it from the other direction variable that we have listed. You can see this all on line 9.

# Next, we can start to think about how we can combine the encrypt and decrypt functions together. We need a way of storing a piece of text, so we create a variable called end_text. This will be an empty string, then we have to loop through the text that we pass over. So, this is where we can create the for loop again. We create the position variable to grab the index of the each letter that is in the start_text, this can be seen on line 12. Once we have that it will save the index of the letter to that variable. This will happen for each letter. 

# Now, we need to set up a conditional that will decode(decrypt) if the user types in decode and encode(encrypt)if the user types in encode. Instead of doing if and elif conditionals we can just check for if the cipher direction was decode. In this case, we would take the shift amount and multiply it by -1. Outside of the if conditional we can define our new position and set it to equal the previous position plus the shift amount. 

# The reason this is an easier way of doing this is because, let's say we had a shift amount of 5 and we wanted to encode our text, well the new position is obviously going to be the previous position plus five. It's exactly the same as subtraction, like so if the position is 12 and multiply the shift amount of 5 * -1, we get -5. When we add 12 + -5 we get 7! This is exactly the same as subtraction. 

# Since we have gotten that squared away our next step will be tap into our end_text and to add it it by getting hold of the letter at the new position in the aplhabet. Once all of that is done, we can finally print the result. However we need to change our print statement to be a bit more dynamic. 