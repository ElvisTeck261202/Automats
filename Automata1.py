#Functions which represents each node of the automata
def S1 (userInput, index):
    print('S1')
    if userInput[index] == 'a':
        index += 1
        S2(userInput, index)
    else:
        print(f'The character {userInput[index]} is invalid in the node S1')

def S2 (userInput, index):
    print('S2')
    if userInput[index] == 'c':
        index += 1
        S3(userInput, index)
    else:
        print(f'The character {userInput[index]} is invalid in the node S2')

def S3 (userInput, index):
    print('S3')
    if userInput[index] == 'c' or userInput[index] == 'b':
        index += 1
        S3(userInput, index)
    elif userInput[index] == 'a':
        index += 1
        S4(userInput, index)
    else:
        print(f'The character {userInput[index]} is invalid in the node S3')

def S4 (userInput, index):
    print('S4')
    if userInput[index] == 'a' or userInput[index] == 'c':
        index += 1
        S4(userInput, index)
    elif userInput[index] == 'b':
        index += 1
        S5(userInput, index)
    else:
        print(f'The character {userInput[index]} is invalid in the node S4')
    
def S5 (userInput, index):
    print('S5')
    print('Your word is a valid input!!')

#Variables used
invalidWord = False
index = 0
userInput = input("Use a word in base of the following alphabet = (a,b,c)")
print(len(userInput))

#For cycle to autenticate that the word is valid
for i in userInput:
    if i != 'a' and i != 'b' and i != 'c' and len(userInput) < 4:
        invalidWord = True
        break

#If sentence in case the word was valid or not
if invalidWord == False:
    print('Valid Word')
    S1(userInput, index)
else: 
    print('Invalid Word, start again')
