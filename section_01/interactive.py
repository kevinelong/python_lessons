
while True:

    user_text = raw_input("Enter Command: (dance, sleep or quit):")

    if "quit" == user_text:
        break #  Break out of the while loop
    if "dance" == user_text:
        print "\tDancing Complete."
    elif "sleep" == user_text:
        print "\tSlept."
    elif "" == user_text:
        print "Blank line is not a command."
    else:
        print "Unknown Command: " + user_text
