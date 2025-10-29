#WAP to find the distance between two points in 2-D space.
import math
plan1x=float(input("Enter a x co-ordinates in plan-1:"))
plan1y=float(input("Enter a y co-ordinates in plan-1:"))
plan2x=float(input("Enter a x co-ordinates in plan-2:"))
plan2y=float(input("Enter a y co-ordinates in plan-2:"))

dis=math.sqrt((plan1x-plan2x)*(plan1x-plan2x)+(plan1y-plan2y)*(plan1y-plan2y))
print("distance between two point is :",dis)