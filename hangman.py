# Hangman Game by Bad McProgammer!
import random
ws =  open('word-list.txt')
index = 0
picked = random.randint(0, 25)
for w in ws:
    if index == picked:
        pick = w
    index = index+1
import sys
guessed =[]
word=pick[:-1]
solve = "?" * len(word)
lives = 9
while solve != word:
    for index in range(len(word)):
        print(solve[index],end="")
        print(" ",end="")
    print()
    print('lives =',  end='')
    print(lives)
    print('please guess')
    guess =input()
    if guess in guessed:
        print('you guessed that already')
    elif (guess in word) == False:
        print('that\'s not in the word')
        lives = lives - 1
    else:
        print('you got a letter')
        for index in range(len(word)):
            if word[index] == guess:
                solve = solve[0:index] + guess + solve[index+1:]
    guessed = guessed + [guess]
    if lives < 0:
        print('you died, sorry!')
print('you solved the hangman game')
print('run again to play again')
