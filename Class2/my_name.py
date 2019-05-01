def welcome():
    print "What's your name?"
    name = raw_input()
    print "Hello {}!".format(name)

welcome()

print "Enter your first number:"
x = raw_input()
print "Enter your second number:"
y = raw_input()

#converting strings to int 
x = int(x)
y = int(y)


def add(x,y):
    print ("print the total: {0}".format(x + y))

add(x, y)
    
