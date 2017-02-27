#Use a while-loop only to loop forever, and that means probably never. This only applies to Python; other languages are different.
#Use a for-loop for all other kinds of looping, especially if there is a fixed or limited number of things to loop over.

i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num
