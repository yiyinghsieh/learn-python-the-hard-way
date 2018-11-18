# ex31_1.py

print "There have three gift boxs, which one do you choice: 1 or 2?" 

gift = raw_input("> ")

if gift == "1":
    print "You can choose your birthday gift boxs number 1 or 2?"

    box = raw_input("> ")
    if box == "1":
        print "There have a cheese cake."
    elif box == "2":
        print "There have a jelly candys."
    else:
        print "Let me think about it."


elif gift == "2":
    print "You can take a vacation. Japan or Taiwan?"
    
    vacation = raw_input("> ")

    if vacation == "Japan": 
        print "The scene is beautiful."
    elif vacation == "Taiwan":
        print "The night market food is delicious."
    else:
        print "Stay at home to celebrate it."
else:
    print "Maybe we can save some money."
