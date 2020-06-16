'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
  # Your code here
    p = {0:1, -1:1}   # products ([:i] for pos. keys, [i:]-neg. keys)
    n = len(arr)
    for i in range(1,n):
        p[i]    = arr[i-1] * p[i-1]  # prod of elements left of i
        p[-i-1] = arr[-i]  * p[-i]   # prod of elements right of i
    return [p[i]*p[-n+i] for i in range(n)]


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
