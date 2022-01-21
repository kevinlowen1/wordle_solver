from urllib import robotparser
import pandas as df
from pyparsing import Regex
from wordlist import load_words
from wordRemover import regexTester

# def regexTester(newWordList, wordAttempt, tentativeLetters, successNumbers):
#    for letter in tentativeLetters:
#       # create column for whether the word contains the necessary letters and filter the wordlist
#       newWordList['stillValid'] = newWordList.word.str.contains(letter, na=False, case=False)
#       #check against dataframe for validity
#       newWordList = newWordList[newWordList.stillValid == True]
   
#    for number in successNumbers:
#       #what is the letter at the number specified bby the user
#       letterToCheck = wordAttempt[int(number)-1]
#       # create regex wildcards as necessary before letter
#       regexPatternStart = '.' * (int(number)-1)
#       # create regex wildcards as necessary after letter
#       regexPattternEnd = '.' * (5 - int(number))
#       #create regex pattern to check against
#       regexPattern = regexPatternStart + letterToCheck + regexPattternEnd
#       #check regex pattern against dataframe to create updated column for validity
#       newWordList['stillValid'] = newWordList.word.str.contains(regexPattern, na=False, case=False, regex=True)
#       #check against dataframe for validity
#       newWordList = newWordList[newWordList.stillValid == True]

#    ##replace letters in wordAttempt with nothing
#    for letter in tentativeLetters:
#       wordAttempt = wordAttempt.replace(letter, '')

#    for letter in wordAttempt:
#       newWordList.drop(columns=['stillValid'])
#       # create column for whether the word contains the necessary letters and filter the wordlist
#       newWordList['stillValid'] = newWordList.word.str.contains(letter, na=False, case=False)
#       #check against dataframe for validity
#       newWordList = newWordList[newWordList.stillValid != True]

#    return(newWordList)


if __name__ == "__main__":
   fiveLetterWords = load_words()

   #get info on first word attempted
   print('The first word you should try is SERAI')
   firstWord      = input('Enter the first word you tried: ')
   tentative      = input('Enter any letters that were tentative or correct (yellow or green.)  For example if you guessed BROWN and the B was yellow and the N green, enter BN:    ')
   tentativenums  = input('Enter position of any letters that were tentative (yellow.)  For example if you guessed BROWN and B was tentative, enter 1:    ')
   success        = input('Enter position of any letters that were correct (green.)  For example if you guessed BROWN and both the R and W were green, enter 24:    ')
   #create new possible words from user input
   fiveLetterWords = regexTester(fiveLetterWords, firstWord, tentative, tentativenums, success)
   print('these are some of the possible words that are left: \n') 
   print(fiveLetterWords.word.to_string(index=False))

   #get info on second word attempted
   secondWord     = input('Enter the second word you tried: ')
   tentative      = input('Enter any letters that were tentative or correct (yellow or green.)  For example if you guessed BROWN and the B was yellow and the N green, enter BN:    ')
   tentativenums  = input('Enter position of any letters that were tentative (yellow.)  For example if you guessed BROWN and B was tentative, enter 1:    ')
   success        = input('Enter position of any letters that were correct (green.)  For example if you guessed BROWN and both the R and W were green, enter 24:    ')
   #create new possible words from user input
   fiveLetterWords = regexTester(fiveLetterWords, secondWord, tentative, tentativenums, success)
   print('these are some of the possible words that are left: \n') 
   print(fiveLetterWords.word.to_string(index=False))
   

   #get info on third word attempted
   thirdWord      = input('Enter the third word you tried: ')
   tentative      = input('Enter any letters that were tentative or correct (yellow or green.)  For example if you guessed BROWN and the B was yellow and the N green, enter BN:    ')
   tentativenums  = input('Enter position of any letters that were tentative (yellow.)  For example if you guessed BROWN and B was tentative, enter 1:    ')
   success        = input('Enter position of any letters that were correct (green.)  For example if you guessed BROWN and both the R and W were green, enter 24:    ')
   #create new possible words from user input
   fiveLetterWords = regexTester(fiveLetterWords, thirdWord, tentative, tentativenums, success)
   print('these are some of the possible words that are left: \n') 
   print(fiveLetterWords.word.to_string(index=False))


   #get info on fourth word attempted
   fourthWord      = input('Enter the fourth word you tried: ')
   tentative      = input('Enter any letters that were tentative or correct (yellow or green.)  For example if you guessed BROWN and the B was yellow and the N green, enter BN:    ')
   tentativenums  = input('Enter position of any letters that were tentative (yellow.)  For example if you guessed BROWN and B was tentative, enter 1:    ')
   success        = input('Enter position of any letters that were correct (green.)  For example if you guessed BROWN and both the R and W were green, enter 24:    ')
   #create new possible words from user input
   fiveLetterWords = regexTester(fiveLetterWords, fourthWord, tentative, tentativenums, success)
   print('these are some of the possible words that are left: \n') 
   print(fiveLetterWords.word.to_string(index=False))

   #get info on fifth word attempted
   fifthWord      = input('Enter the fifth word you tried: ')
   tentative      = input('Enter any letters that were tentative or correct (yellow or green.)  For example if you guessed BROWN and the B was yellow and the N green, enter BN:    ')
   tentativenums  = input('Enter position of any letters that were tentative (yellow.)  For example if you guessed BROWN and B was tentative, enter 1:    ')
   success        = input('Enter position of any letters that were correct (green.)  For example if you guessed BROWN and both the R and W were green, enter 24:    ')
   #create new possible words from user input
   fiveLetterWords = regexTester(fiveLetterWords, fifthWord, tentative, tentativenums, success)
   print('these are some of the possible words that are left: \n') 
   print(fiveLetterWords.word.to_string(index=False))


