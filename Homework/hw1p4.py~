"""
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
"""

prompt = '> '
sentence = ''
mycount = ''

def getInput():
    print "Write any sentence that contains number, letters and other chars"
    sentence = raw_input(prompt)
    if (len(sentence.split()) < 1):
        print "Come on, write something down..."
        getInput()
    else:
        print "Yeap, that's a good sentence"
    return sentence

def count_chars(mytext):
    count_letters = 0
    count_digits = 0
    count_others = 0
    for char in mytext:
        if char.isalpha():
            count_letters += 1
        elif char.isdigit():
            count_digits += 1
        else:
            count_others += 1
    return count_letters, count_digits, count_others

mycount = count_chars(getInput())
print "LETTERS %s \n DIGITS %s \n OTHERS %s" % mycount
