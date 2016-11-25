import random
from time import sleep

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
    ifile = open(i + ".txt", "w+")
    recipient = random.choice(peopleremaining)
    while not CoupleUnitTest(i, recipient):
        fault += 1
        if fault >= 100:
            raise Exception("Could not complete, bad pair.")
        recipient = random.choice(peopleremaining)
    ifile.write("You will be giving a gift to " + recipient + ".")
    peopleremaining.remove(recipient)
    testing.append(i + " is giving a gift to " + recipient)

if verbose:
    for i in testing:
        print(i)

