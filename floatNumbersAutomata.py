def S1 (word, index, alphabet):
    print('S1')
    if word[index] in alphabet:
        index += 1
        S2(word, index, alphabet)
    elif word[index] == '.':
        print('Sorry, this is an invalid character in the node S1')

def S2 (word, index, alphabet):
    print('S2')
    if word[index] in alphabet:
        index +=1
        S2(word, index, alphabet)
    elif word[index] == '.':
        index += 1
        S3(word, index, alphabet)
    else:
        print('Sorry, this is an invalid character in the node S2')

def S3 (word, index, alphabet):
    print('S3')
    if word[index] in alphabet:
        index += 1
        S4(word, index, alphabet)
    elif word[index] == '.':
        print('Sorry, this is an invalid character in the node S3')

def S4 (word, index, alphabet):
    print('S4')
    if index == len(word):
        print('This is a valid word for this automata')
    elif word[index] in alphabet:
        index += 1
        S4(word, index, alphabet)

#Variables used in the automata
word = input('Write a word with the following alphabet (0-9, .): ')
alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
state = 'S1'
track = ['S1']
index = 0
dot = 0
invalidWord = False

#Cycle to check if the word has an invalid character or more than one dot
for i in word:
    if i not in alphabet:
            invalidWord = True 
    elif i == '.':
        dot += 1

if invalidWord == False and dot == 1:
    if word[len(word) - 1] == '.':
        print('Sorry, your word cannot end in a dot') 
    else:
        S1(word, index, numbers)
elif invalidWord == True:
    print('Sorry, your word has an invalid character')
elif dot == 0:
    print('Sorry, the number has to be a float number')
elif dot > 1:
    print('Sorry, your word has more than one dot')

    