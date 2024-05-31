weight = input("Weight: ")
k = input("(k)g or (l)bs: ")

if k == "k":
    weight = float(weight) / 0.45
    print("Weight in lbs: " + str(weight))

elif k == "l": 
    weight = float(weight) *  0.45
    print("Weight in kg: " + str(weight))
