# Write a program to read in words from the keyboard one at a time until the word "quit" is typed.
# Store them in a list then print them alphabetically
words=[]
argument=True
while argument:
    word=input("Insert word here")
    if "quit" in word:
        words.sort()
        print(words)
    else:
        words.append(word)