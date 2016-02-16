

'''
1. String concatenation:
        	x="cat"
        	y="dog"

        	What does x+y equal?
            catdog

Write a for loop that takes a list of words
words=["cat","dog","fish","sugar glider","frog","rabbit"]
makes it into one string and prints out that string.
'''

words = ["cat","dog","fish","sugar glider","frog","rabbit"]
x = ''
replace_with = "cat"
to_replace = "dog"
counter = 0
for word in words:
    counter += 1
    if word == to_replace:
        word = replace_with
    x += word+" "
print(x)

for index in range(len(words)):
    print(index,words[index])
# 2. Now INSIDE the for loop, search for a particular word and change it in the
# final string. Eg search for "cat" and change it to "dog" before you create the string.

# 3. Change your for loop to use the index instead of the items.
