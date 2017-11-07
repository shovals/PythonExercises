import random
HeadsCounter = 0.0
TailsCounter = 0.0

for i in range(50):
    selection = random.randint(0,1)
    if selection == 0:
        print "Tails"
        TailsCounter += 1
    else:
        print "Heads"
        HeadsCounter += 1

heads = float(HeadsCounter / 50 * 100)
tails = float(TailsCounter / 50 * 100)

print ""
print "---- Summary ----"
print "Head was selected {} of the times, which is {}%".format(HeadsCounter,heads)
print "Tails was selected {} of the times, which is {}%".format(TailsCounter,tails)