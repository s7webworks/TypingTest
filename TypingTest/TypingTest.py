
#Simple script to test words per minute typing speed
#common words will be displayed, the final count will
#display count and accuracy when the timer expires.




# import time library 
import time
import random
import string 


#set timer for 60 seconds
t_end = time.time() + 60 
correct = 0
incorrect = 0
attempts = 0
accuracy = 0
words = []
    
def easy():
# English wordlist
    words = ["apple", "boats", "clock", "brags", "fruit", "elder", "berry", "float", "grape", "honey", "kiwis", "lemon", "mango", "north", "maint", "older", "peach", "quite", "rated", "straw", "tests", "buggy", "vines", "water", "melts", "xigua", "toast", "frogs", "zebra", "roads","words","never"]

    return words

#TODO: Create medium skill words with random Capitalized English words

def dificult():

# Generate 100 random words
    for i in range(100):
        letters = ''.join(random.choice(string.ascii_lowercase) for j in range(5))
        words.append(letters)
    return words

#TODO: Create insanity skill words with dificult words AND special chars
    
print("-=-=-=- Welcome :) -=-=-=-=")
#TODO: Create promt for instructions 

print("Skill level: (E)asy (M)edium or (H)ard? ")




skill = input("[e/m/h]? : ")    #skill selection prompt
if (skill == "e")  or (skill == "E") or (skill == "Easy") or (skill == "EASY"):
    words = ["apple", "boats", "clock", "drags", "fruit", "elder", "berry", "float", "grape", "honey", "kiwis", "lemon", "mango", "north", "maint", "older", "peach", "quite", "rated", "straw", "tests", "buggy", "vines", "water", "melts", "xigua", "toast", "frogs", "zebra", "roads","words","never"]

elif (skill == "m") or (skill == "M") or (skill == "medium") or (skill == "Medium") or (skill == "MEDIUM"):
    words = ["apple", "boats", "clock", "drags", "fruit", "elder", "berry", "float", "grape", "honey", "kiwis", "lemon", "mango", "north", "maint", "older", "peach", "quite", "rated", "straw", "tests", "buggy", "vines", "water", "melts", "xigua", "toast", "frogs", "zebra", "roads","words","never"]

    for i in range(len(words)):
        words[i] = words[i].title()
else:
    dificult()                #random 5 character letter combos non-english wordlist
    
                              #main program loop
while time.time() < t_end:
    for word in random.sample(words, 1):
        print(word)
        attempts += 1
        a=input("?")
        if a == word:
            correct += 1
            
            continue
        else:
            incorrect += 1
            
            continue

#Calculate and display results
accuracy = (correct / attempts ) * 100
print("=-=-=- Results: -=-=-= \nCorrect: " + str(correct) + " \nErrors: " + str(incorrect) + " \n Total WPM: " + str(attempts) + "\nAccuracy: " + str(accuracy) )

        
#    break

