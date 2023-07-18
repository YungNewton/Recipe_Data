# This function is used to check if a provided string is a well-formed QC test result string.
def isValidString(s):

    # We start by importing numpy, a powerful library for handling numerical data
    import numpy as np

    # We first check if the given 's' is a string and that it is not 'NaN' (not a number). If it's not a string or it's NaN, we return False and zeroes for all outputs.
    if not isinstance(s, str) or s is np.nan:
        return False, 0, 0, 0

    # The QC string should start with 'Q', if not, it is not valid and we return False and zeroes
    if not s.startswith('Q'):
        return False, 0, 0, 0

    # We split the string into 'batches' at each 'Q'
    batches = s.split('Q')[1:]
    
    # We then initialize the counts of total tests, passed tests, and defects to zero
    total_tests = 0
    passes = 0
    defects = 0

    # For each batch in our batches...
    for batch in batches:

        # A valid batch must contain 'p' and 'd', if not, it is not valid and we return False and zeroes
        if 'p' not in batch or 'd' not in batch:
            return False, 0, 0, 0

        # We find the positions of 'p' and 'd'
        p_index = batch.index('p')
        d_index = batch.index('d')

        # Depending on the positions of 'p' and 'd', we split the batch into three parts: start, middle, end
        if p_index < d_index:
            start, middle, end = batch[:p_index], batch[p_index+1:d_index], batch[d_index+1:]
        else:
            start, middle, end = batch[:d_index], batch[d_index+1:p_index], batch[p_index+1:]

        # Each part must be a number (hence the isdigit function), if not, it is not valid and we return False and zeroes
        if not start.isdigit() or not middle.isdigit() or not end.isdigit():
            return False, 0, 0, 0

        # The numbers should not start with zero (unless they are zero), if they do, it is not valid and we return False and zeroes
        if (len(start) > 1 and start.startswith('0')) or (len(middle) > 1 and middle.startswith('0')) or (len(end) > 1 and end.startswith('0')):
            return False, 0, 0, 0

        # The start number (total tests) should not be zero, if it is, it is not valid and we return False and zeroes
        if int(start) == 0:
            return False, 0, 0, 0

        # The start number should equal the sum of the middle and end numbers (total tests = passes + defects), if not, it is not valid and we return False and zeroes
        if int(start) != int(middle) + int(end):
            return False, 0, 0, 0

        # If all conditions are met, we add the numbers to our total counts
        total_tests += int(start)
        passes += int(middle)
        defects += int(end)

    # If we make it through all batches without returning False, the string is valid and we return True along with our counts
    return True, total_tests, passes, defects
