""" A dictionary in python is a data type that stores values in terms of key -value pair. The Key of a dictionary need to be unique or immutable while the value of the dictionary can be an int, string, tuple, list or even another dictionary. A dictionary is introduced by the use of the curly braces. """

phonebook = {
    "Jena" : 25477452542,
    "Bena" : 25663214621,
    "Tina" : 25754212112
    }

print("My Phonebook dictionary is: ", phonebook)

# To access the values of a dictionary we use the key.
print("Tina's phone number: ", phonebook["Tina"])

print("==========================")

player = {
    "name" : "Messi",
    "Age"  : 39,
    "teams" : ["Miami", "PSG", "Argentina", "Barcelona"],
    "more" : {
        "Children" : 3,
        "networth" : 4.5,
        "citizenship" : ("US", "Spain", "Argentina")
    }
}

# Task: Print out Argentina.
print(player["more"]["citizenship"][2])

print("==========================")


print("==========================")
# Boolean - It evaluates to either true or false
isSunny = True
isRaining = False

print("Is today sunny in Nairobi? ", isSunny)
print(type(isSunny))