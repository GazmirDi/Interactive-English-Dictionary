import json
import difflib 

data = json.load(open("data.json"))

def meaning(word):
    if word in data:
        return data[word]
    else:
        return "This word doesn't exist. Please double check it!"


word = input ("Enter a word: ").lower()


print(meaning(word))    

