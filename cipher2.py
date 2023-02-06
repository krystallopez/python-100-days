from art_cipher import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}")


print(logo)

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")

# To make this code look a bit cleaner, we are going to combine the decrypt and encrypt functions into one function called caesar(). We will get rid of the if conditionals and rework our code bit so that we can get it looking much cleaner.

# First, we are going to create our new function called caesar(). The function will take in 3 parameters: the text, the shift, and the direction. We call the text parameter start_text(since we could be passed the plain_text or the cipher_text). Then we will have shift_amount, and the last one will be called cipher_direction to differentiate it from the other direction variable that we have listed. You can see this all on line 8.

# Next, we can start to think about how we can combine the encrypt and decrypt functions together. We need a way of storing a piece of text, so we create a variable called end_text, as seen on line 9. This will be an empty string, then we have to loop through the text that we pass over. So, this is where we can create the for loop again. We create the position variable to grab the index of the each character that is in the start_text, this can be seen on line 13. Once we have that it will save the index of the letter to that variable. This will happen for each char. If the character is in the alphabet list then lines 14-16 will run. This will only occur if the user chooses "encode", if the user chooses "decode" then the if conditional will run prior to the function being called. 

# I have set up the conditional in order to decode(decrypt) if the user types in decode and encode(encrypt)if the user types in encode. Instead of doing if and elif conditionals, you can just check to see if the cipher direction was decode. If so, we would take the shift amount and multiply it by -1. The reason for this is because it is an easier way of performing subtraction, let's say we had a shift amount of 5 and we wanted to encode our text, well the new position is obviously going to be the previous position plus five. It's exactly the same as subtraction, so if the position is 12 and multiply the shift amount of 5 * -1, we get -5. When we add 12 + -5 we get 7! This is exactly the same as subtraction.

# Since we have gotten that squared away our next step will be tap into our end_text and to add to it by getting hold of the character at the new position in the alphabet. Once all of that is done, we can finally print the result. However we need to change our print statement to be a bit more dynamic. So we interpolate our cipher_direction variable. However if the character is not in the alphabet list it will be encoded. Only characters that are in the alphabet list will be encoded. (This is all done in lines (14-18))

# Now we are going to account for if the user adds in a number or symbol in as their input. We have also added some ASCII art as well. We import logo from art_cipher file and print it at the top of our code so that this is what the user sees when they run the code in the terminal. We need to create a way for the code to stillr run if a user enters in a shift_amount that is over 25. As you can see on line 30, we have done, basically python will continue to divide the shift_amount by 26 as many times as needed until it gets to the final point where it can no longer be divided fully and we end up with a remainder. Now let's say the user wants to keep playing, lines 33-37 will run after the decoded/encoded output is given and if the user wants to continue they can type in yes and the program starts all over again, if they type in no, the console prints "goodbye" and the program ends.  
