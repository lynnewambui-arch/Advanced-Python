# Conditional statements.
# if ...  else statement

# number = int(input("Enter your number: "))


# if number > 0:
#     print("The number is positive.")
# else:
#     print("The number is negative.")

print("=========================")
# create a dictionary with student's details like name, email, admissionNo and password. Prompt the student to enter the password for him to be able to access the student portal. By use of an if statement, check whether the entered password is correct to navigate him to the portal otherwise if the password entered is incorrect, pass a message to block the student from accessing the student portal.

print("=========================")
# Combining the logical and comparison operators together.
age = int(input("Enter your current age: "))
has_id = False

if age >= 18 and has_id:
    print("You can join us for the function.")
else:
    print("Sorry, you do not qualify to join us.")

print("=========================")
# Below is an example of a nested if Statement.
if age >= 18:
    if has_id:
        print("You qualify. you can join us")
    else:
        print("You don't qualify because you need an ID")
else:
    print("You don't qualify because you are underage.")

print("=========================")
# By use of a nested if statement, check whether a person is allowed to drive a vehicle or not. For a person to be able to drive a vehicle, he need to be 18 or above years of age and has a valid driver's license.