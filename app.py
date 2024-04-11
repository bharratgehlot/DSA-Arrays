#Hamngman Game using Arrays in python [DSA]

import random

#List of words for the game

fruits = ["apple","orange","bnana", "mango", "papaya", "grapes"]
vegs = ["lady finger", "potato", "Tomato", ]

def choose_word():
  return random.choice(fruits)


def display_word(word, guessed_letters):
  




def hangman():
  word = choose_word()
  guessed_letters = []
  attempts = 5

  print("Welcome to the Hangman Game!")
  print("Try to guess the word in 5 attempts")

while attempts > 0:
  print("\n" + display_word(word, guessed_letters))
