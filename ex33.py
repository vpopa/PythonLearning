i = 0
numbers = []

#while i < 6:
#    print "At the top i is %d" % i
#    numbers.append(i)
#
#    i = i + 1
#    print "Numbers now: ", numbers
#    print "At the bottom i is %d" % i
    
def my_function(nr):
    for i in range(0, int(nr)+1):
        print "At the top i is %d" % i
        numbers.append(i)
        
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

my_function(15)

print "The numbers: "

for num in numbers:
    print num