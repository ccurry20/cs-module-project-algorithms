'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    result = 0
    for i in arr:
        result ^= i #XOR sets the result to 1 if either, but not both, of the corresponding bits in the two operands is 1.
    return result  #return the result // 1 integer

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")