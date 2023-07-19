
# def unpair_at_most(n: int, pairs: list[tuple[int,int]]) -> list[int]:
#     if n <= 0:
#         return []
#     else:
#         pairs[:n] = [num for pair in pairs[:n] for num in pair]
#         return pairs[:2*n]


# # unpairAtMost 0 [] == []
# # unpairAtMost 5 [] == []
# # unpairAtMost -1 [] == []
# # unpairAtMost 2 [(10,20),(30,40)] == [10,20,30,40]
# # unpairAtMost 2 [(10,20),(30,40),(50,60)] == [10,20,30,40]
# # unpairAtMost 4 [(10,20),(30,40),(50,60)] == [10,20,30,40,50,60]
# # unpairAtMost -1 [(10,20),(30,40),(50,60)] == []

# print(unpair_at_most(0, []))  # Expected output: []
# print(unpair_at_most(5, []))  # Expected output: []
# print(unpair_at_most(-1, []))  # Expected output: []
# print(unpair_at_most(2, [(10,20),(30,40)]))
# print(unpair_at_most(2, [(10,20),(30,40),(50,60)]))
# print(unpair_at_most(4, [(10,20),(30,40),(50,60)]))
# print(unpair_at_most(-1, [(10,20),(30,40),(50,60)]))


from typing import Callable, List, Tuple
import copy

from typing import Callable



Input = tuple[int, list[tuple[int,int]]]
FunctionSignature = Callable[[int, list[tuple[int,int]]], list[int]]

test_cases = [
    (0, []),
    (5, []),
    (-1, []),
    (2, [(10,20),(30,40)]),
    (2, [(10,20),(30,40),(50,60)]),
    (4, [(10,20),(30,40),(50,60)]),
    (-1, [(10,20),(30,40),(50,60)]),
]


def model_solution(n: int, pairs: list[tuple[int,int]]) -> list[int]:
    return [] if n <= 0 else [num for pair in pairs[:n] for num in pair]

def unpairAtMost(n: int, pairs: List[Tuple[int, int]]) -> List[int]:
    if n <= 0:
        return []
    else:
        pairs[:n] = [num for pair in pairs[:n] for num in pair]
        return pairs[:2*n]

import copy

def checker(model_solution: FunctionSignature, student_solution: FunctionSignature, test_cases: list[Input]) -> bool:
    for test_case in test_cases:
        # We use copy.deepcopy to create completely separate copies of the test cases for each function
        student_test_case = copy.deepcopy(test_case)
        model_test_case = copy.deepcopy(test_case)

        student_answer = student_solution(*student_test_case)
        expected_answer = model_solution(*model_test_case)

        if student_answer != expected_answer:
            return False

    return True


# print(unpair_at_most(0, []))  # Expected output: []
# print(unpair_at_most(5, []))  # Expected output: []
# print(unpair_at_most(-1, []))  # Expected output: []
# print(unpair_at_most(2, [(10,20),(30,40)]))
# print(unpair_at_most(2, [(10,20),(30,40),(50,60)]))
# print(unpair_at_most(4, [(10,20),(30,40),(50,60)]))
# print(unpair_at_most(-1, [(10,20),(30,40),(50,60)]))
print(checker(model_solution, unpairAtMost, test_cases))

print(unpairAtMost(0, []))  # Expected output: []
print(unpairAtMost(5, []))  # Expected output: []
print(unpairAtMost(-1, []))  # Expected output: []
print(unpairAtMost(2, [(10,20),(30,40)]))
print(unpairAtMost(2, [(10,20),(30,40),(50,60)]))
print(unpairAtMost(4, [(10,20),(30,40),(50,60)]))
print(unpairAtMost(-1, [(10,20),(30,40),(50,60)]))