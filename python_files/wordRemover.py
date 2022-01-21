import pandas as df

def regexTester(newWordList, wordAttempt, tentativeLetters, tentativenums, successNumbers):
    #rremove worrds without valid letters
    for letter in tentativeLetters:
        # create column for whether the word contains the necessary letters and filter the wordlist
        newWordList['stillValid'] = newWordList.word.str.contains(letter, na=False, case=False)
        #check against dataframe for validity
        newWordList = newWordList[newWordList.stillValid == True]
   
    #remove words without valid letters in correct spots
    for number in successNumbers:
        #what is the letter at the number specified bby the user
        letterToCheck = wordAttempt[int(number)-1]
        # create regex wildcards as necessary before letter
        regexPatternStart = '.' * (int(number)-1)
        # create regex wildcards as necessary after letter
        regexPattternEnd = '.' * (5 - int(number))
        #create regex pattern to check against
        regexPattern = regexPatternStart + letterToCheck + regexPattternEnd
        #check regex pattern against dataframe to create updated column for validity
        newWordList['stillValid'] = newWordList.word.str.contains(regexPattern, na=False, case=False, regex=True)
        #check against dataframe for validity
        newWordList = newWordList[newWordList.stillValid == True]

    #remove words that have valid letters at invalid locations 
    for number in tentativenums:
        newWordList.drop(columns=['stillValid'])
        #what is the letter at the number specified bby the user
        letterToCheck = wordAttempt[int(number)-1]
        # create regex wildcards as necessary before letter
        regexPatternStart = '.' * (int(number)-1)
        # create regex wildcards as necessary after letter
        regexPattternEnd = '.' * (5 - int(number))
        #create regex pattern to check against
        regexPattern = regexPatternStart + letterToCheck + regexPattternEnd
        #check regex pattern against dataframe to create updated column for validity
        newWordList['stillValid'] = newWordList.word.str.contains(regexPattern, na=False, case=False, regex=True)
        #check against dataframe for validity
        newWordList = newWordList[newWordList.stillValid != True]

    ##replace letters in wordAttempt with nothing if tthe letter is valid
    for letter in tentativeLetters:
        wordAttempt = wordAttempt.replace(letter, '')
    #remove words that contain invalid lettters
    for letter in wordAttempt:
        newWordList.drop(columns=['stillValid'])
        # create column for whether the word contains the necessary letters and filter the wordlist
        newWordList['stillValid'] = newWordList.word.str.contains(letter, na=False, case=False)
        #check against dataframe for validity
        newWordList = newWordList[newWordList.stillValid != True]


    return(newWordList)