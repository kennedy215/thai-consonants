name = raw_input("Welcome to the multilple choice test...What is your name?" )
age = raw_input("How old are you? ")
movie = raw_input("""What kind of movies do you like?\n
A. Horror\n
B. Comedy\n
C. Action\n
""" )

Q1Answer = "A"
score = 0

if (age > 20):
    score = score + 1
    print "Ok your old enough"
if (Q1Answer == movie ):
    score = score + 1
    print " %s You love horror movies your awesome! Your only %s years old! Your cool score is %s" % (name, age, score)

else:
    print " %s It's past your bed time, your only %s years old! Your cool score is %s" % (name, age, score)
