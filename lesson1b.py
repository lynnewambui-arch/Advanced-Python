mynumber = 10
number2 = 10

sum = mynumber + number2
print("The sum of the numbers is: ", sum)

# 3. List : A list is a collection of items that are inside of square brackets.
"""A lis is mutable i.e you change the contents of a list. You can add/append alter a list in different ways. """

mylist = ["Russia", "Ukraine", "UK", "France", "Belarus", "Italy", "Germany"]

print(mylist)
print(type(mylist))

mylist.append("Denmark")
mylist.append("Poland")
print(mylist)

# it reverses the ordering of the list
mylist.reverse()
print(mylist)

# sort function it is used to rearrange based on the Alphabetical order
mylist.sort()
print(mylist)

# pop : you can remove based on a given index
mylist.pop(3)
print(mylist)

# remove : Based on the value name of item
mylist.remove("Poland")
print(mylist)

# Extend : used to add multiple items at once
mylist.extend(["Portugal", "Switzerland"])
print(mylist)

# Insert : used to add an item to list at a specific index
mylist.insert(0, "Finland")
print(mylist)

# Below is a  list inside of a list
list2 = [["James", "Tony","Bernard", "Jeremiah"], ["Joyce", "Mary", "Oscar", "Martha"], ["Brian", "Edward","Joseph", "Linet"]]
print("The name is: ",list2[0][2])

# create two lists with 3 items each and then join the two list to make one big list



# 4 : Tuple : This is an immutable type of a list meaning : it is unchangeable. The way you define the tuple at first it remains the same upto the end.

presidents = ("Uhuru", "Ruto", "Yoweri", "Mnangangwa", "Ramaphosa")
print(presidents)
print(type(presidents))

# Note: Below code will bring an error:
# presidents.append("Suluhu")
# print(presidents)

presidents.pop(2)
print(presidents)