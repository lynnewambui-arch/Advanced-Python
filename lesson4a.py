#Python Functions
#a function is a block of code that performs a given task.
#We have two main functions,i.e:
#1.User defined functions->They are created by the user/
#2.In-built->They come with the installation of the python interppreter.eg.print(),pop(),reverse(),sort()
###1. User defined function. To create a user defined function, we use the def keyword followed by the name of the function, parenthensis and at the end of the function defination there is a full colon. The lines that comes next are indented and they mark the body of the function.
#To invoke/call the function, you do so outside of the function body by the use of the function name.# type: ignore ###
def greeting():
    print("Hello there ,how are you doing")


greeting()
def addition():
              number1=12
              number2=13
              number3=20
              sum=number1+number2+number3
              print("The sum of the number is:", sum)

addition()
print("=======")
for greet in range(1,6):
        greeting(),print(greet)

print("===========")

#Below is a function that demonstrates how to pick details froom the user  on the keyboaed

def multiplication():  
    number1=int(input("Enter the first number:"))
    number2=int(input("Enter the second number:"))
    product=number1*number2
    print("The product of the two numbers is:", product)
multiplication()

#Create a functionnthat is able to calculate the simple interest after a person invested 75000 for 5 years  and the rate was 6.5% per year.
def simple_interest():
        principle=75000
        rate=6.5
        time=5
        interest=(principle*rate*time)/100
        print("The simple interest is:",interest)
simple_interest()
