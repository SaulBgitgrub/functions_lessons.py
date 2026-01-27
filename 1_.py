# Methods, Help & Documentation Practice #1
# Remove the characters to the left of our main text:

#Function = A block of reusable code
#           place () after the function to invoke it

#Return = statement used to end a function
#       and send a result back to the caller

# def add(x, y):
#     z = x + y
#     return z
# def subtract(x,y):
#     z = x + y
#     return z
# def multiply(x, y):
#     z = x * y
#     return z
# def divide(x,y):
#     z = x / y
#     return z
# print(add(1, 2))
# print(divide(4, 2))
# print(multiply(2, 3))
# print(subtract(6, 2))

def create(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create("Sponge", "Bob")
#???

def display_invoice(user_name,amount, due_date):
    print(f"Hello {user_name}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")
display_invoice("Joe", 100.01, "Day")
# ,
def happy_birthday():
    print("Happy birthday to you")
    print()

# def happy_birthday(name,age):
#     print(f"Happy birthday to {name}")
#     print(f"You are {age} years old")
#     print()
# happy_birthday("Joe, 30")



# happy_birthday()
# happy_birthday()
# happy_birthday()

# print("Happy birthday to you!")
# print()
# print("Happy birthday to you!")
# print()
# print("Happy birthday to you!")
# print()


# :

# %

# _

# #

# Use the lstrip() method. Print the result to the screen:

# ",:_#,,,,,,:::____##Total_ _Pyt%on,,,,,,::#"

# Search the documentation for the requested method to learn how it works. You can use intermediate variables if you need them.


# Methods, Help & Documentation Practice #2
# Add the element "orange" as the fourth element of the following list fruits, using the insert() method:

# fruits = ["mango", "banana", "cherry", "plum", "grapefruit"]

# Search the documentation for the requested method to know how it works.

# Methods, Help & Documentation Practice #3
# Check if the sets below are isolated (that is, they have no elements in common), using the isdisjoint() method. Store this result in the isolated_sets variable:

# phone_brands = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
# tv_brands = {"Sony", "Philips", "Samsung", "LG"}
# Search the documentation for the requested method to know how it works.

