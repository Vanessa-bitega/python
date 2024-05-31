course = "my pets"
#upper () returns a new string does not affect the original;
#print(course.upper() )'

print(course.replace('y','i'))
print('y' in course)

items = ["aets", "cvets", "mnets", "wwts"]
print(sorted(items, key=str.lower))# this sort the list regardless if one starts with a lower or upp case and it does not modify the original list

print(items.sort())# modifies the og list and stars with the uppercase and eadss the lowercase after

#tuples is a list that is immutable meaning it is constant can't be changed
#and instead of [] like normal lists it uses ()



#sets are unordered and unindexed
#dictionary or dict are key,value pairs i.e {"key": "value}:keys are immutable while value can be anything you like