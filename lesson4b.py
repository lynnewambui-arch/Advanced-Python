#Functions with parameters
#PARAMETERS ARE VALUES THAT GET PASSED AS ARGUMENTS WHEN invoking a function.

def greeting(name):
    print("Hello ", name, "How have you been?")
greeting("John")

def message(name):
    print("Greeting,",name,"You are kindly reminded to atttend the meeting to be held on 16th October 2026")


print("===========")
message("Benerd Kamotho")
message("Linnet Wambui")
message("Christina Maabinyana")

def addition(number1,number2,number3):
    sum=number1+number2+number3
    print("The sum of the numbers is:",sum)
addition(10, 20, 5)


print("===========")
#Create a function that accepts a parameter that is able to calculate the simple interest after a person invested 75000 for 5 years  and the rate was 6.5% per year.

def simple_interest(principle, rate, time):
        interest=(principle*rate*time)/100
        print("The interest gained is:",interest)

simple_interest(75000, 6.5, 5)
simple_interest(45000,7,4)

print("===========")
 #Create a function that accepts parameters to caalculate the BMI of a person whose weight is 55kg and height is 1.75 meters.Formulae BMI=weight/(height*height)
def calculate_BMI(weight, height):
    BMI=weight/(height*height)
    print("The BMI of the person is:",BMI)

calculate_BMI(55,1.75)