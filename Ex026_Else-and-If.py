#Every if-statement must have an else.
#If this else should never run because it doesn't make sense, then you must use a die function in the else that prints out an error message and dies, just like we did in the last exercise. This will find many errors.
#Never nest if-statements more than two deep and always try to do them one deep.
#Treat if-statements like paragraphs, where each if-elif-else grouping is like a set of sentences. Put blank lines before and after.
#Your boolean tests should be simple. If they are complex, move their calculations to variables earlier in your function and use a good name for the variable.

people = 30
cars = 40
trucks = 15


if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."
