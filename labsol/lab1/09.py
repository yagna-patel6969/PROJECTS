#WAP to get the distance from user into kilometer, and convert it into meter, feet, inches and centimeter.

km=float(input("Enter a distance in KM:"))
print("given distace in meter:",km*1000)
print("given distance in cm",km*1000*100)
print("given distance in feet",(km*3280.84))
print("given distance in inch",km*39370.1)