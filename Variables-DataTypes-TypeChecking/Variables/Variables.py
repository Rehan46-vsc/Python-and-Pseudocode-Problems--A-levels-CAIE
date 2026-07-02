#This is a comment,these will not come up in your final output and just act as a medium of me to guide you without causing any errors
# #As we just learnt the gist of variables and what they mean in coding we will be learning how variables can be used in python 
#and how they differ from other programming languages and pseudocode

#Variables are defined with the assignment operator, “=”. Python is dynamically typed, meaning that variables can be assigned without declaring their type, and
#that their type can change.(DOES NOT HAPPEN IS PSEUDOCODE) Values can come from constants, from computation
#involving values of other variables, or from the output of a function.

#We can use variables in a calculation like this:

product=2*3
#the output of 2*3 would be stored in the variable "product"

#Variables can also store lists:
Student_name=[]

#Or store just strings or names like this:
StudentName="Rehan"
#Variables can be reassigned. Here "Rehan" is simply the current value stored in the variable.



#Lets try using multiple variables and storing them in one variables

m=43
x=21
c=63

y=m*x+c

print(y)

#As seen in the examples, you can use the print() command in order to show the
#values stored in variables on the screen.

#Python also allows multiple inputs like this:
b, a, d = 1, 2, 3
print(b, a, d)

#Python doesn't have true constants, but by convention:

PI = 3.14159
MAX_SIZE = 100
#Variables written in ALL CAPS are intended not to change.

#Lastly:
#Here are some basic rules for Python variables:
#1 A variable name must start with a letter or the underscore character
#2 A variable name cannot start with a number
#3 A variable name can only contain alpha-numeric characters (A-z, 0-9) and
#underscores
#4 Variable names are case-sensitive, e.g., amount, Amount and AMOUNT
#are three different variables
#5 Second reassignment overwrites the original value


