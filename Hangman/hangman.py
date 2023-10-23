#!/usr/bin/env python3


import random
from Hangman.words import words
import string

def get_valid_word(words):
    word = random.choice(words) #randmoly chooses something from the list
    while '-' in word or ' ' in word: # as long as this statement is true keep iterating
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed
    
    lives = 6
    
    # getting userinput
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b'cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - O R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: '.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters: #if this is a valid character in the alphabet that I haven't used yet
            used_letters.add(user_letter) #add this to used_letters set
            if user_letter in word_letters: #if the letter that I guessed is in the word
                word_letters.remove(user_letter) #remove letters from word_letters if they have alrady been used

            else:
                lives = lives - 1 # takes away a life if wrong
                print('Letter is not in word.')
        elif user_letter in used_letters:
            print('You have already used that character. Please try again')
        
        else: 
            print('Invalid character. Please try again.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You loss, sorry!')
    print('You guessed the word', word, '!!')
hangman()