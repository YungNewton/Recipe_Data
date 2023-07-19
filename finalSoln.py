# Item 3a:

# In the given code, the issue arises from the way Python handles mutable data types like lists. When you pass the list as an argument to a function in Python, it is passed by reference, not by value.
# This means that if the list is modified within the function, the changes will persist outside of it, which is not always the intended behavior.

def unpairAtMost(n: int, pairs: List[Tuple[int, int]]) -> List[int]:
    if n <= 0:
        return []
    else:
        pairs[:n] = [num for pair in pairs[:n] for num in pair]
        return pairs[:2*n]
