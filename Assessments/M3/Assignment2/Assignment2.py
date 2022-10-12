import random as rd
while 1:
    a=rd.randint(10,100)
    b=rd.randint(10,100)
    if a>=80 :
     if b>80:
        print("Hazard")
     else:
        print("High Temp")
    else:
        print("All Good")