# Item 3a:

# In the given code, the issue arises from the way Python handles mutable data types like lists. When you pass the list as an argument to a function in Python, it is passed by reference, not by value.
# This means that if the list is modified within the function, the changes will persist outside of it, which is not always the intended behavior.
# Consider a correct implementation of unpair_at_most as below:
def unpair_at_most(n: int, pairs: list[tuple[int,int]]) -> list[int]:
    pairs[:n] = [pair for pair in pairs[:n] for num in pair]
    return pairs
# Now suppose the test case (2, [(10,20),(30,40),(50,60)]) is being checked. The function unpair_at_most modifies the input pairs in-place to get the result, changing pairs to [(10,20),(30,40)]. 
# The list comprehension operates in-place, and therefore, the original pairs list in the test_cases is also modified. 
# This discrepancy is what causes the checker function to return False, as the expected_answer is generated using the modified input.


# Item 3b:

# We can fix this issue by ensuring that the input arguments to the function are not modified. 
# We do this by creating a copy of the input list before passing it to the function. 
# Here's the modified version of the checker function:

def checker(model_solution: FunctionSignature, student_solution: FunctionSignature, test_cases: list[Input]) -> bool:
    for test_case in test_cases:
        # We make a deep copy of the test_case to prevent mutation of the original data
        test_case_copy = copy.deepcopy(test_case)

        student_answer = student_solution(*test_case_copy)
        expected_answer = model_solution(*test_case_copy)

        if student_answer != expected_answer:
            return False

    return True
# Here, we use the deepcopy function from the copy module to create a new copy 