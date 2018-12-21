# NON-EXISTING WORDS

# importing library
import json
# loading data in json format as dictionary format in Python
data = json.load(open("words.json"))


#function
def getMeaning(word):
    if word in data:
        return data[word]
    else:
        return "The word is not present, Recheck it"


userWord = input("Enter a word:")
print(getMeaning(userWord))
