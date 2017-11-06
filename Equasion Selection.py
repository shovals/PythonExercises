# A calculator for common equasions
import math

# Select an equation from the list
print "Welcome to the equasion calculator ---"
print "--------------------------------------"
print """
1 - Area of a circle
2 - Area of an ellipse
3 - Area of an equalateral triangle
"""

equasion = int(raw_input("Select the equasion to solve:"))



if equasion == 1:
    print "--- Area of a circle"
    radius = float(raw_input("Enter the circle radius:"))
    print "Area of circle = {0:0.2f}".format(math.pi * radius*radius)
elif equasion == 2:
    print "--- Area of an ellipse"
    radius1 = float(raw_input("Enter the first circle radius:"))
    radius2 = float(raw_input("Enter the second circle radius"))
    print "Area of ellipse = {0:0.2f}".format(math.pi * radius1 * radius2)
elif equasion == 3:
    print "--- Area of an equalateral triangle"
    hight = float(raw_input("Enter the height of the triangle:"))
    print "Area of equalateral triangle = {0:0.2f}".format(hight**2*math.sqrt(3)/3)
else:
    pass