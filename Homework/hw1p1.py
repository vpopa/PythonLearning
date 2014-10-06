"""
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

# string method
#numbers = ''

# list method
numbers = []

for i in range(2000, 3201):
    if (not(i % 7) and i % 5):
        #add numbers that fulfill the conditions to the string
        #numbers = numbers + str(i) + ','
        
        #add numbers that fulfill the conditions to the list
        numbers.append(i)
    i = i + 1

#remove last char from the string which contains the saved numbers
#numbers = numbers[:-1]    

#print the results
print "The numbers divisible by 7 but not by 5 are: %r" % numbers
