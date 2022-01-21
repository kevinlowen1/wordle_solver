wordle_solver
========================

you should only need to modify the path of the wordlist on your machine in wordlist.py
(Im terrible with referencing things so sorry about that)

The program will ask for user input on:
1) what they entered as their word
2) what they got yellow (ie. 4 if the fourth letter was yellow)
3) what they got green (ie. 5 if the fifth letter was green)

Then the user will recommend a restricted list of words.

If i felt like it this could be improved by looking at the available wordlist and recommending words that would restrict the list the most when they are proven wrong.
For example, if we know 3 letters, but there are >100 words left as possible, don't try and guess the correct word.  
Instead guess a word that would restrict the possible words the most by finding new letters and removing impossible letters (so don't repeat letters until under 100 possible words).

As is the program works fine, but usually not until the fourth or fifth try will you get it right, by implementing the above you would get a smaller possible list after your second turn.


wordlist taken from below, reference there for copyright or sub your own word list in: 
https://github.com/dwyl/english-words