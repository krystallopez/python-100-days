# Challenge 1: Picking a Random Word and Checking Answers - Step 1 
#-------------------------------------------------------
import random # Need this module to randomly choose word from word_list

word_list = ["aardvark", "baboon", "camel"]

#Todo-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list) 
# This assigns the randomly chosen word from the word_list to the variable using the random module 

#Todo-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter: ").lower() 
# This stores the user's input and then converts the input to lower case


#Todo-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in chosen_word:
  if letter == guess: 
    print("Right")
  else: 
    print("Wrong")


# This for in loop will go through each letter in the chosen_word variable. Inside of the for in loop we can check to see if the letter that we currently lookin is equal to the letter that the user guesses. If the letter is correct then the console will print "Right" if not then the console will print "Wrong".


# Challenge 2: Replacing Blanks with Guesses - Step 2 
#----------------------------------------------------

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
word_length = len(chosen_word) # This stores the length of the chosen_word in a variable, to make your code more readable.
for letter in chosen_word:
  display += "_"
print(display) 

# Printing it outside of the loop will show the full list of underscores that are added for each letter of the word
# This for in loop adds an underscore for every letter in the chosen_word to the display list 

# A range function could be used as well 
# for letter in range(len(chosen_word)):
#   display += "_"
# print(display)
  
guess = input("Guess a letter: ").lower()

#Todo-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter

    

# Using a for loop and the range function, this for loop is going to run for as many times as there are letters in the word and it is also going to give us a number, a position to work with. This number indicates where the letter is at in the word, similarly we can think of letter as being the index of the word. So for example if the user guesses the letter a, it will be added at index 0, 1, and 5.

# On line 32, we assign the value of the letter variable to the position of the letter in the chosen_word, this will allow us to check to see if the letter is equal to the letter that the user guessed. Once we have done that, we can then get a hold of our display and get the item at the current position and then set that equal to the letter and remove the else statement entirely. 

#Todo-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

print(display)

# Challenge 3: Checking if the player has won- Step 3 
#----------------------------------------------------

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#Todo-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

# we need to wrap a while loop around the block code so that the user can continue to guess a letter and will stop once the user has guessed all of the letters. We create the variable end_of_game and set it to false to begin becuase it is not yet the end of the game. While end_of_game or while not end_of_game, we will repeat the code block, until all all of the blanks are filled. If there are no more blanks then end_of_game is changed to true and the user has won the game. 

end_of_game = False


while not end_of_game:
  guess = input("Guess a letter: ").lower()

#Check guessed letter
  for position in range(word_length):
      letter = chosen_word[position]
      print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
      if letter == guess:
          display[position] = letter

  print(display)

  if "_" not in display:
    end_of_game = True
    print("You Win")

