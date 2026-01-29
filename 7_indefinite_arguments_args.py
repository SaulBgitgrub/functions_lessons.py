# def tea_order(customer_name, tea_type, *args):
#     print(customer_name, "ordered a", tea_type, "tea")
#     print("Args contains: ", args)
#     for arg in args:
#         print("   - add:", arg)

# tea_order("Alice","chamomile")
# tea_order("Bob", "black","oat")
# tea_order("Tony","Black", "Oat", "Honey")

# def tea_order(customer_name, tea_type, **kwargs):
#     print(customer_name, "ordered a", tea_type, "tea")
#     for key, value in kwargs.items():
#         print("   - add:", key, ":", value)

# tea_order("Alice","chamomile")
# tea_order("Bob", "black",milk="oat")
# tea_order("Tony","Black", milk="Oat", sweetener="Honey")

def tea_order(customer_name, tea_type, *args, **kwargs):
    print(customer_name, "ordered a", tea_type, "tea")
    for arg in args:
        print("   - Add", arg)
    for key, value in kwargs.items():
        print("   - add:", key, ":", value)

# eves_extras = ("milk": "almond", "sweetener": "sugar", "flavor": "lemon")
# tea_order("Eve", "green", **eves_extras)
tea_order("Alice","chamomile")
tea_order("Bob", "black",milk="oat")
tea_order("Tony","Black", milk="Oat", sweetener="Honey")

# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.
# def sum_squares(4,5,6):
#     for number in sum_squares:

def sum_squares(*args): #
    total = 0
    for num in args:
        total += num **2 #Return total sum of squares


        return total
print(sum_squares(1, 2, 3))
print(sum_squares(4, 5, 6, 7, 8, 8))

# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).


# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).

def absolute_sum(*args):
    total = 0 #Initialize total to 0
    for num in args: #Iterate through each argument
        total+= abs(num) # Add the absolute value of the number to total
        #First time through loop: total = 0 + abs(-1) = 1
        #second time through loop: total = 2 + abs(2) = 3
        #Third time through loop: total = 3 + abs(-3)

        return total
print(absolute_sum(-1, 2, -3)) #Example Usagfe
print(absolute_sum(-10, 20, -30, 40, -50))

# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.
def personal_numbers(name, *args):
    return f"{name}. the sum of your numbers is {sum(args)}"
print(personal_numbers("Jacob", 3, 4))

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"