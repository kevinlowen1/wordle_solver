from datetime import date


import pandas as df

def load_words():
    with open('C:\\Users\\Kevin.DESKTOP-9D0VMK8\\Documents\\Projects\\WORDLE_SOLVER\\wordlist.txt') as word_file:
        valid_words = set(word_file.read().split())

    #create  df
    valid_words = list(valid_words)
    valid_words = df.DataFrame(valid_words)
    valid_words.columns = ['word']
    
    #add length column to df
    valid_words['length']  = valid_words['word'].str.len()

    #filter df to only 5 letter words
    valid_words = valid_words[valid_words.length == 5]

    # print(valid_words)
    return valid_words


if __name__ == '__main__':
    fiveLetterWords = load_words()
    # demo print
    print(fiveLetterWords)