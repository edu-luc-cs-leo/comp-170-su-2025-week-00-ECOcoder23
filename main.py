#-----------------------------------------------------------------------------

# Lab 0
# Problem 1
"""
1. first_name, is a valid name in python, because it is snake case, which is when we use '_' instead of spaces between words.
2. 2nd_name, is an invalid variable name as it does not begin with either a letter or underscore, but with a number
3. age, is a valid variable name as it starts with a letter and contains only letters, numbers or underscores (as is convention in snake case)
4. total_amount, is a valid variable name as it follows the snake case convension of starting with either a letter or underscore and containing only letters, numbers or underscores
5. while, is an invalid variable name as it uses one of Python's reserved words
6. Student, is a valid variable name as it begins with a letter and contains no special characters
7. my-variable, is an invalid variable name as it contains the special character "-"
8. for, is an invalid variable name as it uses one of Python's reserved words
9. _temp, is a valid variable name as it begins with an underscore and contains no special characters 
10. value#, is an invalid variable name as it contains the special character "#"
"""
# Problem 2
"""
1. calculate_total, is a valid function name as it starts with a letter and contains only either letters or underscores (snake case convention)
2. 3rd_function, is an invalid function name as it begins with a number (and not either a letter or underscore)
3. print_values, is a valid function name as it begins with a letter and contains only letters and undercores
4. find-values, is an invalid function name as is contains the special character "-"
5. def, is an invalid function name as it uses one of Python's reserved words 
6. updateProfile, is an invalid function name as the words "update" and "Profile" are not separated by an underscore
7. my_function, is a valid function name as it begins with a letter and contains only letters and underscores
8. try, is an invalid function name as uses one of Python's reserved words
9. init_data, is a valid function name as it begins with a letter and contains only letter and underscores
10. value@function, is an invalid funtion name as it contains the special character "@" and does not separate the words "value" and "function" with an underscore
"""
# Problem 3
"""
Your solution goes here


"""
#-----------------------------------------------------------------------------
# Homework 0
# Problem 1
def is_even(x):
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


# Problem 2
def split_dict_to_lists(some_dict: dict):
  
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.
    return list_keys, list_values


# Problem 3
def evaluate_expression(boolean1, boolean2, string_operator)->bool:
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.   
        

# Problem 4
def find_odd_numbers(a_list: list)-> list:
    """
    a_list is just one example of a the kind of input you could recieve
    a_list = [3,4,5,6,7]
    odd_list = [3,5,7]
    """
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.
        
# Problem 5
def calculate_average(numbers_list: list)-> int:
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


import sys
def test(did_pass):
   """ Print the result of a test. """
   linenum = sys._getframe(1).f_lineno
   msg = "Test at line {0} {1}.".format(linenum, "ok" if did_pass else "FAILED")
   print(msg)



def test_is_even():
    test(is_even(4) == True)
    test(is_even(5) == False)
    test(is_even(0) == True)

def test_split_dict_to_lists():
    keys, values = split_dict_to_lists({'a': 1, 'b': 2})
    test(keys == ['a', 'b'])
    test(values == [1, 2])
    keys, values = split_dict_to_lists({'c': 3, 'd': 3})
    test(keys == ['c', 'd'])
    test(values == [3, 3])

def test_evaluate_expression():
    test(evaluate_expression(True, False, 'and') == False)
    test(evaluate_expression(True, True, 'and') == True)
    test(evaluate_expression(True, False, 'or') == True)
    test(evaluate_expression(False, True, 'not') == True)

def test_find_odd_numbers():
    test(find_odd_numbers([1, 2, 3, 4, 5]) == [1, 3, 5])
    test(find_odd_numbers([2, 4, 6]) == [])

def test_calculate_average():
    test(calculate_average([10, 20, 30, 40, 50]) == 30.0)
    test(calculate_average([5, 5, 5, 5]) == 5.0)


def test_suite():
    test_is_even()
    test_split_dict_to_lists()
    test_evaluate_expression()
    test_find_odd_numbers()
    test_calculate_average()

test_suite()  # Here is the call to run the tests
