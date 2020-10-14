#Diy Calculater
#Intrduction Code
print("Hi , I' am Calc Bot ,")
name = input("Whats your name ?:")
print("Hello " + name + ". Nice to meet you !" )
command = input("Press [Enter] To Continue:")
print("IN ORDER TO CALCULATE AGAIN YOU HAVE TO RUN THE PROGRAM AGAIN")

#Calculations:
command = input("Press [Enter] To Continue:")
print(command)

func = input("[Enter] Your Function-[D],[M],[A],[S]:")
print(func)

print(command)
print("Welcome to my Program ,here you can do Text Mathematical Calculations.")
print("......................................................................")
print("(!) Help")
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
print("Functions:")
print("For Division type---------[D]")
print("For Multiplication type---[M]")
print("For Addition type---------[A]")
print("For Subtraction type------[S]")
print("*Note*:You are only allowed to do all the functions*")
print("! YOU ARE ONLY ALLOWED TO CALCULATE ONCE,")
#Division:
print("First we will start with -D-")

print("D")
def division(D):
    num1 = input("Enter a Number: ")
    num2 = input("Enter another Number: ")
    result = float(num1)/float(num2)
    D = result
    print(D)
division("/")
command = input("Press [Enter] To Continue:")
print(command)

#Multiplcation:
print(",and now with -M-.")

print("M")
def multiplication(M):
    num1 = input("Enter a Number: ")
    num2 = input("Enter another Number: ")
    result = float(num1)*float(num2)
    M = result
    print(M)
multiplication("*")
command = input("Press [Enter] To Continue:")
print(command)

#Addition:
print("Time for-A-")

print("A")
def addition(A):
    num1 = input("Enter a Number: ")
    num2 = input("Enter another Number: ")
    result = float(num1)+float(num2)
    A = result
    print(A)
addition("+")
command = input("Press [Enter] To Continue:")
print(command)

#Subtraction:
print("-S-")

print("S")
def subtraction(S):
    num1 = input("Enter a Number: ")
    num2 = input("Enter another Number: ")
    result = float(num1)-float(num2)
    S = result
    print(S)
subtraction("-")
command = input("Press [Enter] To Continue:")
print(command)

print("WOW YOU DID IT")
print("DID YOU ENJOY IT?")
f_b = input("Give ur feedback:")
command = input("Press [Enter] To Continue:")
print(command)

#End
print("IN ORDER TO CALCULATE AGAIN YOU HAVE TO RUN THE PROGRAM AGAIN")

msg = "DISCORD"
print("*Message me on " + msg + " about ur Feedback*")

print("Thank You !")


command = input("Press [Enter] To Continue:")
print(command)
