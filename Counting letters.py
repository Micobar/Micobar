# counting how many letters are in a string that was entered by a user

string = input(": ") # this kind of input because of the dict
count = 0
x = {} # making a dict

for i in string:
    if i in x:
        x[i] += 1 # if i is in x then adds 1
    else:
        x[i] = 1 # if i not in x this means it has showed up once, then x holds the value of 1

print(x)