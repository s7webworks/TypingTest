# TypingTest
================
Overview
================

A simple typing test written in Python 3 by Scotty Myers

This script will present the user with five letter words or combinations depending on selected skill level. 
The user is prompted to type the displayed "word" as fast as possible, and submit the response by pressing
the <Enter> key.

Once the first word is displayed the program will run for 60 seconds issuing a new "word" when the current
word has been typed and submitted.  The program will track the number of words displayed, the number of
correct submissions, as well as incorrect attempts. 

Results will be calculated after 60 seconds annd displayed to the user. The results displayed are:

Total "words" displayed and attempts submitted in 1 minute will reveal the users Words Per Minute (WPM)
speed. 

      -- The overall WPM typing speed is based on number of 5-letter words submitted in 60 seconds,
         both correct and incorrectly typed words will count toward WPM. 
         
      -- Correct submissions will be counted and used to determine accuracy.
      
      -- Incorrect attemps will be counted and used to determine accuracy.
      
      -- Typing Accuracy will be calculated and displayed to the user after 60 seconds.
      
================
Skill Levels
================

Easy:  This skill level will randomly select common English words consisting of 5 letters.

Medium:  This skill level will randomly select common English words of 5 letters, including
         proper capitalization.

Hard:  This skill level uses random 5-letter combinations to form non-English "words" to
       test knowledge of the actual keyboard layout versus mucsle memory of commonly used
       words and keystroke combinations.
       
================
TODO
================
       
Use the getch() function from the curses module to read keyboard input without requiring
the user to press Enter after each word.  Limiting each attempt to set number of keystrokes will
remove the ability to <Backspace> and fix errors as well as remove the need to press <Enter>
after each word is typed.

Create Insanity skill level by including random special characters, random capitalized letters, 
as well as random numbers with random letters. 

Create a save file to log previous results including time and date history, display performance
reports / track progress changes.

