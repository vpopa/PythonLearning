"""
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
"""

prompt = '> '
given_words = ''
words_sorted = ''
split_words = ''
words = ''

def getInput():
    print "Write some words separated by comma"
    given_words = raw_input(prompt)
    return given_words
        
def breakWords(given_words):
    return given_words.split(',')
  
def sortNewString(unsorted_list):
    return sorted(unsorted_list)
   
#read_from = getInput()
#split_words = breakWords(read_from)
#words_sorted = sortNewString(split_words)

words_sorted = sortNewString(breakWords(getInput()))

print "The words sorted and in a comma-separated sequence are: %s" % ','.join(words_sorted)
