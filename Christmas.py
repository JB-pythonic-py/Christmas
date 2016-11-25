import random

people = ["Jordan", "Jeni", "Sidney", "Zach", "Tonya", "Derryl", "Trevor"]
peopleremaining = ["Jordan", "Jeni", "Sidney", "Zach", "Tonya", "Derryl", "Trevor"]
testing = []
couple1 = ["Jordan", "Jeni"]
couple2 = ["Sidney", "Zach"]
couple3 = ["Tonya", "Derryl"]


def CoupleUnitTest(person1, person2):
    if person1 in couple1 and person2 in couple1:
        return False
    if person1 in couple2 and person2 in couple2:
        return False
    if person1 in couple3 and person2 in couple3:
        return False
    if person1 == person2:
        return False
    return True

verbose = False

for i in people:
    fault = 0
    ifile = open(i + ".txt", "w+")  # Opens a text file with the giver's name.
    recipient = random.choice(peopleremaining)  # Picks a random person to be the recipient.
    while not CoupleUnitTest(i, recipient):  # Runs the couple unit test to be sure it's not a couple.
        fault += 1
        if fault >= 100:
            raise Exception("Could not complete, bad pair.")  # If it fails 100 times in a row, raises error.
        recipient = random.choice(peopleremaining)  # If it is a couple, it tries to select someone else instead.
    ifile.write("You will be giving a gift to " + recipient + ".")  # Saves the recipient to the giver's text file.
    peopleremaining.remove(recipient)  # Removes the recipient from the list of choices remaining.

    if verbose:
        testing.append(i + " is giving a gift to " + recipient)

if verbose:
    for i in testing:
        print(i)

