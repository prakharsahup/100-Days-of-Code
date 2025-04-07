import random


wordList = ["python", "java", "javascript", "html", "css", "ruby", "swift", "kotlin", "typescript", "csharp"]
myWord = random.choice(wordList)
wordLen = len(myWord)
output = []
lives = 6
stage = 6
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


game_over = False

for i in myWord:
    output += "_"

while "_" in output and not game_over:
    for i in range(len(myWord)+5):
        if "_" in output:
            print("Guess a letter: ")
            guessLetter = str(input())
            
            if guessLetter in myWord:
                for j in range(len(myWord)): 
                    if guessLetter == myWord[j]:
                        output[j] = guessLetter
            else:
                lives -= 1
                stage -= 1
                
            print(stages[stage])        
            print(output)
        else:
            print("Game Over")
            print("You win")
        if lives == 0:
            print("Game Over")
            print("You Lose")
            game_over = True




