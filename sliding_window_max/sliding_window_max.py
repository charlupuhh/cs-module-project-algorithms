'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    answer = []
    win_start = 0
    win_end = k
    end = len(nums) - k + 1

    for num in range(0, end):
        window = nums[win_start:win_end]
        max_num = max(window)
        answer.append(max_num)
        win_start += 1
        win_end += 1
    return answer


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
