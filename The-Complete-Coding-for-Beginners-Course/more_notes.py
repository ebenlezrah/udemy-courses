a = [1, 2, 3]
b = (1, 2, 3) # Tuple - a list that cannot be changed after it is created
c = {1, 2, 3} # Set - a list that cannot have duplicate values
d = {'name': 'John', 'age': 25} # Dictionary - a list that has key-value pairs

e = ("english", "spanish") 
f = [[1,2], [3,4]] # List of lists
g = [(1,2), (3,4)] # List of tuples

list = [("a", "b"), ("c", "d"), ("e", "f")]
list[1][0] # c

number_list = "[1, 2, 3]"
print(number_list[0]) # [
# strings can also be read as a list of characters

import ast
print(ast.literal_eval(number_list)[0]) # 1