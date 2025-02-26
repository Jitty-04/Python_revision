# item1 = {2,3,4,"hello","hey",5,6,0}

# print(item1)

# item = set(range(1,10))

# item.add("hello") # add an element to a list

# item.copy() # return shallow copy of set

# item.pop() # remove any random element from the set

# item.remove("hello") # Remove an element from a set; it must be a member.
                      # If the element is not a member, raise a KeyError.

# print(item)

items1 = {1, 2, 3, 4, 5}
items2 = {"hello", True, "welcome", False}

result = items1.union(items2)  # Return the union of sets as a new set.
                               # (i.e. all elements that are in either set.)

print(result)

result = items1.intersection(items2)
print(result)

result = items1.difference(items2)  # Remove elements from items1 that are already in items2
print(result)

result = items2.difference(items1)  # Remove elements from items2 that are already in items1
print(result)
