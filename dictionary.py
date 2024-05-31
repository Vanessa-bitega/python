#Dictionaries

#Here is an example of a dictionary:

dog = {"name": "Bob", "age": 8 }

dog["name"]="syd"
#print(dog.get("name"))

# get method to get , this can add a default value

#print(dog.get("color","red")) # this will make red the default color if there is none
#print(dog.pop("name")) # this method will return the item and delete it
#print(dog.popitem("name")) # this method will return and remove the last key value pair inserted into the dictionary


#to add a new element in a dict

#dog["favorite food"] = "bones"

#to delete a dict
#del dog["age"]
#print(dog)

#print(dog.keys())
#print(dog.values())
#print(len(dog)) checks the length of the dictionary



#
#print(list(dog.items()))

########SETS##########

#sets are immutble ,kinda looks like dict but without the keys and they are unordered thisnk about them as mathemathical set

set1 = {"roger","jin"}
set2 = {"jin"}
set4= {"van","red"}

#intersection
intersect = set1 & set2
print(intersect)
print(set1.intersection(set2))

#union
mood = set1 | set2  #return 
print(mood)
#print(set1.union(set4))