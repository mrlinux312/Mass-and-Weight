#Mass and weight program
#weight over 500 = too heavy
#weight under 100 = too light
print("Mass and weight")
print("")
mass = float(input("Please enter mass in kilograms"))
weight = mass * 9.8
print(f" The weight of this object is {weight:.2f} newtons")
if weight > 500: print("This object is too heavy")
if weight < 100: print("This object is too light")