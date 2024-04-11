#Hamngman Game using Arrays in python [DSA]

import random

#List of words for the game

fruits = ["apple","orange","banana", "mango", "papaya", "grapes"]
vegs = ["Lady finger", "Potato", "Tomato","Onion" ]

def choose_word():
  return random.choice(fruits)


def display_word(word, guessed_letters):
  display = ""
  for letter in word:
    if letter.lower() in guessed_letters:
      display += letter + ""
    else:
      display += "_ "  
  return display    





def hangman():
  word = choose_word()
  guessed_letters = []
  attempts = 5

  print("Welcome to the Hangman Game!")
  print("Try to guess the word in 5 attempts")

  while attempts > 0:
   print("\n" + display_word(word, guessed_letters))
   guess = input("Enter a Letter: ").lower()

   if guess in guessed_letters:
     print("You already guessed that letter")

   elif guess in word:
     guessed_letters.append(guess)
   if all(letter in guessed_letters for letter in word):
       print("Congrats! you guessed right", word)
       break  
     
   else:
     attempts -= 1
     print("Incorrect guess. You have", attempts, "attempts remaining." ) 

  if attempts == 0:
     print("Sorry, you have zero attempts left. The word was:", word) 


hangman()     
