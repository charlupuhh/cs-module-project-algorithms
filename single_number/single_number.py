'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# done
def single_number(arr):
    while len(arr) > 1:
        removed = arr.pop(0)
        if removed not in arr:
            return removed
        arr.pop(arr.index(removed))
    return arr[0]

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")