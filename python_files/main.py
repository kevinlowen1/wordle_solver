from urllib import robotparser
import pandas as df
from pyparsing import Regex
from wordlist import load_words
from wordRemover import regexTester

if __name__ == "__main__":
   fiveLetterWords = load_words()

   #get info on first word attempted
   print('The first word you should try is SERAI')
   firstWord      = input('Enter the first word you tried: ')
   tentativenums  = input('Enter position of any letters that were tentative (yellow.)  For example if you guessed BROWN and B was tentative, enter 1:    ')
   success        = input('Enter position of any letters that were correct (green.)  For example if you guessed BROWN and both the R and W were green, enter 24:    ')
   #create new possible words from user input
   fiveLetterWords = regexTester(fiveLetterWords, firstWord, tentativenums, success)
   print('these are some of the possible words that are left: \n') 
   print(fiveLetterWords.word.to_string(index=False))

   #get info on second word attempted
   secondWord     = input('Enter the second word you tried: ')
   tentativenums  = input('Enter position of any letters that were tentative (yellow.)  For example if you guessed BROWN and B was tentative, enter 1:    ')
   success        = input('Enter position of any letters that were correct (green.)  For example if you guessed BROWN and both the R and W were green, enter 24:    ')
   #create new possible words from user input
   fiveLetterWords = regexTester(fiveLetterWords, secondWord, tentativenums, success)
   print('these are some of the possible words that are left: \n') 
   print(fiveLetterWords.word.to_string(index=False))
   

   #get info on third word attempted
   thirdWord      = input('Enter the third word you tried: ')
   tentativenums  = input('Enter position of any letters that were tentative (yellow.)  For example if you guessed BROWN and B was tentative, enter 1:    ')
   success        = input('Enter position of any letters that were correct (green.)  For example if you guessed BROWN and both the R and W were green, enter 24:    ')
   #create new possible words from user input
   fiveLetterWords = regexTester(fiveLetterWords, thirdWord, tentativenums, success)
   print('these are some of the possible words that are left: \n') 
   print(fiveLetterWords.word.to_string(index=False))

   #get info on fourth word attempted
   fourthWord      = input('Enter the fourth word you tried: ')
   tentativenums  = input('Enter position of any letters that were tentative (yellow.)  For example if you guessed BROWN and B was tentative, enter 1:    ')
   success        = input('Enter position of any letters that were correct (green.)  For example if you guessed BROWN and both the R and W were green, enter 24:    ')
   #create new possible words from user input
   fiveLetterWords = regexTester(fiveLetterWords, fourthWord, tentativenums, success)
   print('these are some of the possible words that are left: \n') 
   print(fiveLetterWords.word.to_string(index=False))

   #get info on fifth word attempted
   fifthWord      = input('Enter the fifth word you tried: ')
   tentativenums  = input('Enter position of any letters that were tentative (yellow.)  For example if you guessed BROWN and B was tentative, enter 1:    ')
   success        = input('Enter position of any letters that were correct (green.)  For example if you guessed BROWN and both the R and W were green, enter 24:    ')
   #create new possible words from user input
   fiveLetterWords = regexTester(fiveLetterWords, fifthWord, tentativenums, success)
   print('these are some of the possible words that are left: \n') 
   print(fiveLetterWords.word.to_string(index=False))


