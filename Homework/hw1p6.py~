# -*- coding: utf-8 -*-
"""
Write a program which reads from a text file (attached to email) and returns individual words in lowercase and stripped from digits and punctuation. It should return a list of words.
	Problem 6.1
Make a function which takes as input the list of words, and returns a dict that has as a key the word and as value the number of occurrences.
Problem 6.2
Return the word with the most occurrences
"""

import string
#from collections import Counter

mytext_words = []
mytext_unique_words = []

def read_file():
    f = open('speech.txt','r')
    return f.read()

def remove_digits_punctuation(text):
    text = text.translate(None, string.punctuation)
    text = text.translate(None, string.digits)
    return text
      
def get_words(text):
    text = text.split()
    return text
  
def get_unique_words(words_list):
    unique_words = []
    for word in words_list:
        if word not in unique_words:
            unique_words.append(word)
    unique_words.sort()
    return unique_words

# for problem 6.1
def count_words(mylist):
    word_list = {}
    word_count = 0
    for word in mylist:
        word_count = mylist.count(word)
        word_list.update({word:word_count})
    return word_list

# the Counter method - easier ;)
#def count_words(mylist):
#    return Counter(mylist)
#------------------------------------------------------------------------------
# problem 6.0
mytext = read_file()
mytext = remove_digits_punctuation(mytext)
print "The text read from the given file is: %s" % mytext
mytext_words = get_words(mytext)
print '-' * 100
print "The words of the text read from the given file are: \n %s" % mytext_words
mytext_unique_words = get_unique_words(mytext_words)
print '-' * 100
print "The unique ordered words of the text read from the given file are: \n %s" % mytext_unique_words

# problem 6.1
words_dic = count_words(mytext_words)
print '-' * 100
print "The words dictionary which contains each word and number of occurences is: \n %s" % words_dic

# problem 6.2
print '-' * 100
print "The word with the most occurrences is \"%s\" and the word appears %s in the given text" % (max(words_dic, key=words_dic.get), words_dic[max(words_dic, key=words_dic.get)])
