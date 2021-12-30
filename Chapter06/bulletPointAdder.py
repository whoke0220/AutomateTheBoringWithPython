#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard

#import necessary packages
import pyperclip

#get text from the clipboard
text = pyperclip.paste()

#Separate lines and add stars
lines = text.split('\n')

# loop through all items in the list: lines
for i in range(len(lines)):
    #add an asterisk before each line
    lines[i] ='* ' + lines[i]

#combine newly formatted lines back into one string to go to the clipboard
text = '\n'.join(lines)

#send the newly formatted text back to the clipboard
pyperclip.copy(text)
