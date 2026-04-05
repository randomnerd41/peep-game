from PISTON import *

print("loading Peep Game - 1.0_alpha")
print("powerd by the PISTON module.")
wait(5)
clear()

print("Peep the chick was on his small island when a storm came!")
in1 = input("what do you do? 1. go inside 2. stay outside: ")
clear()

points = 0

if in1 == "1":
    print("Peep goes inside and sleeps. your safe! (plus 5 PTS)")
    points += 5
    wait(3)
    clear()
elif in1 == "2":
    print("you get wet and get stuck under a tree for the day.")
    wait(3)
    print("when the storm is over peep goes to bed. (plus 1 PTS)")
    points += 1
    wait(2)
    clear()
else:
    print("you cant do that!")
    wait(2)
    exit()
    
print("You have", points, "points")    
    