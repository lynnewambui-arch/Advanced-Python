# if ... elif ... else conditional statement.
# It is used to evaluates multiple conditions.

# Below is an example of the menu tab on the Bank.

print("Kindly select an option. \n 1. Deposit \n 2. Send Money \n 3. Withdraw Money \n 4. Check Balance \n 5. Exit")

options = int(input("Enter the option : "))


if options == 1:
    print("You selected Deposit")
elif options == 2:
    print("You selected Send Money")
elif options == 3:
    print("You selected Withdraw Money")
elif options == 4:
    print("You selected Check Balance")
elif options == 5:
    print("You selected Exit, Thank you!")
else:
    print("Please enter a valid option from 1 to 5.")

print("================================")
# By use of the if ... elif ... else conditional statement, create a python program that is able to show the working mechanism of the traffic lights.