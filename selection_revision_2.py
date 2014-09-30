#Amin Hagos
#30-09-2014
#Development Exercises Task 2

water_temprature = int(input("please enter the temprature of the water in degrees Centigrade: "))
if water_temprature < 0:
    print("the water is frozen.")
elif water_temprature >= 100:
    print("the water is boiling.")
else:
    print("the water is neither boiling nor frozen.")
    
