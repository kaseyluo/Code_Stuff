# print("hello world")
# print("I am Kasey")
# print("Nice to meet you")



#functions, how to write a function



# def introduction():
# 	print("hello world")
# 	print("I am Kasey")
# 	print("Nice to meet you")

# introduction()


# def introduction_specialized(name):
# 	print("hello world")
# 	print("I am", name)
# 	print("Nice to meet you")

# introduction_specialized("Justin")
# introduction_specialized("Miley")
# introduction_specialized("Kim")
# introduction_specialized("Taylor")
# introduction_specialized("Kanye")
# introduction_specialized("Selena")




# what happens if I call the function before I define it?

# functions with parameters, input/output

# ex, function that sees if the number is greater than 100

# Assignment 1: write a function that takes in user input, and tests if the number is divisible by 10

# user_input = int(input("Type in a number: "))

# def divisible_by_ten(number):
# 	if number % 10 == 0:
# 		print("Your number: ", number, "is divisible by ten")
# 	else:
# 		print("Your number: ", number, "is not divisible by ten")

# divisible_by_ten(user_input)


print("Welcome to my calculator! You will be able to add, subtract, divide, or multiply two numbers")
print("Type 'a' to add, 's' to subtract, 'd' to divide, or 'm' to multiply: ")
operation = input()



def add(number_one, number_two):
	total = number_one + number_two
	return(total)

def subtract(number_one, number_two):
	total = number_one - number_two
	return(total)

def multiply(number_one, number_two):
	total = number_one * number_two
	return(total)

def divide(number_one, number_two):
	total = number_one / number_two
	return(total)


first_number = int(input("Type in one number: "))
second_number = int(input("Type in a second number: "))

if (operation == "a"):
	print(add(first_number,second_number))
elif (operation == "s"):
	print(subtract(first_number,second_number))
elif (operation == "m"):
	print(multiply(first_number,second_number))
elif (operation == "d"):
	print(divide(first_number,second_number))
else:
	print("bleh")



# functions with more than one parameter

# Assignment 2: create a calculator: add, subract, divide, multiply functions, user input two #s

# function that adds two numbers

# obamicon

