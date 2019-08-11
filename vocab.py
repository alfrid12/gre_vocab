import json
import random

#Clear screen
print('\033[H\033[J')

#Import JSON file into json_file variable
with open('unknown_words.json') as json_file:
    data = json.load(json_file)
    vocabWords = data['vocabWords']

    #Get random word from list of words
    randomNumber = random.randint(0, len(vocabWords))
    randomWord = vocabWords[randomNumber]

    #Print word
    print('\n\nWord: ' + randomWord['word'])

    #Wait until user prompts for definition
    userResponse = input('\n\n\n\nPress enter for definition\n')

    #Print definition
    print(randomWord['definition'] + '\n\n\n')

