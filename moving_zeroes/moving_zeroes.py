'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
        # Your code here
    if not arr:
        return
        #if i equals zero, pop from list and append to end
    for i in arr:
        if i == 0:
            newlist = arr.pop(arr.index(i))
            arr.append(newlist)

    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")