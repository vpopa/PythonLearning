"""
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.

Hints:
Use __init__ method to construct some parameters
"""

prompt = '> '
given_text = ''

class MyClass(object):

    def __init__(self):
        print "String not added from console input"

    def getString(self):
        print "Write any text that has at least 3 words"
        given_text = raw_input(prompt)
        if (len(given_text.split()) < 3):
            self.getString()
        else:
            print "Yes, you did it!"
        return given_text

    def printString(self):
        print self.getString().upper()
        
def main():
  c = MyClass()
  c.printString()
  
if __name__ == "__main__":
  main()
