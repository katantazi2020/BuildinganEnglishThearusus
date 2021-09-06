import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("D:\pythonprojects\data.json"))

def translator(w):
    w = w.lower()
#check if the word exists in the dictionary
    if w in data:
        return data[w]
   
#The w.title() method will convert the first letter to uppercase and the
#rest to lowercase. If the program didn't find anything for example "texas" in the first
#condition, then this condition will try to search for "Texas". 
#Even if the user entered "TEXAS" this condition will convert it to "Texas".


    elif w.tittle() in data:
        return data[w.tittle()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input ("Did you mean %s instead? Enter Y if yes, or N if no:" % get_close_matches(w,data.keys())[0])
        if yn == "Y":
             return data [get_close_matches(w,data.keys())[0]]
        elif yn == "N":
             return "The word doesn't exist please check again"
        else:
             return "We did not understand your entry"

#if the word is not existing return this
    else:
        return "The word doesn't exist please check again"
word = input("Enter word: ")
output = translator(word)
if type(output) == list:
     for item in output:
         print(item)
else:
      print(output)
