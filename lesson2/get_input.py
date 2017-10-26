# Input and Printing
# player_input = raw_input("Tell me your name: ")
# print "Hello " + player_input + ", welcome."

name = raw_input("Guess my name (hint: it is hector or keyvan): ")

if name == "hector" or name == "keyvan":
    print "Right!"
    is_cool = True
else:
    print "Wrong!"
    is_cool = False

if is_cool:
    print "Yeah you are cool"
else:
    print "You forgot my name asshole"
