"""
Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

Hints:
Use list[index] notation to get a element from a list.
"""

subject = ["I", "You"]
verb = ["Play", "Love"]
objects = ["Hockey","Football"]

for i in range(0, len(subject)):
    for j in range(0, len(verb)):
        for k in range(0, len(objects)):
            print "%s %s %s" % (subject[i],verb[j],objects[k])
