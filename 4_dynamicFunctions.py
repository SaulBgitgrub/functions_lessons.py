# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.
list = [4,5,6]
def all_positives(list):
    for pos in list:
        if pos < 0:
            return False
    return True





# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000, and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.
list2 = [0, 5, 7, 2000]
def sum_less(list2):
    for sum in list2:
        if sum < 1000 and sum > 0:
            





# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.