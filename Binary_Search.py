"""
Binary Search Implementation

This algorithm has to be used on a list sorted in ascending or descending order.

I am studying Leetcode questions, to prep for a future job interview!

Steps in the alg
    1) Compare x with the middle element
        Matches? We return the middle index.
    2) No match? If x is greater than then middle element,
        then x can only lie in the right half of the list.
        We then re-apply the algorithm for this half.
    3) If x is smaller than the middle element,
        then x can only lie in the left half of the list.
        we then re-apply the algorithm for this half.

Date: 2024-12-10
"""

def binary_search_desc(nums, low, high, target):
    """
        The binary search algorithm code
        """

    # Base Case:
    if high >= low:
        # Get middle
        middle = (high + low) // 2
        # Check middle
        if nums[middle] == target:
            return middle

        # If target is bigger than the value at the middle of the list
        # it can only be in the left side of the list.
        elif nums[middle] < target:
            return binary_search_asc(nums, low, middle - 1, target)

        # If the target is smaller than the value at the middle of the list
        # if can only be in the right side of the list.
        else:
            return binary_search_asc(nums, middle + 1, high, target)

    else:
        # Element is not in the list.
        return False


def binary_search_asc(nums, low, high, target):
    """
    The binary search algorithm code
    """

    # Base Case:
    if high >= low:
        # Get middle
        middle = (high + low) // 2
        # Check middle
        if nums[middle] == target:
            return middle

        # If target is smaller than the value at the middle of the list
        # it can only be in the left side of the list.
        elif nums[middle] > target:
            return binary_search_asc(nums, low, middle - 1, target)

        # If the target is bigger than the value at the middle of the list
        # if can only be in the right side of the list.
        else:
            return  binary_search_asc(nums, middle + 1, high, target)

    else:
        # Element is not in the list.
        return False


def main():
    """
    Main Function
    """

    nums = [9,8,7,6,5,4,3,2,1]
    target = 3
    # check asc/desc
    if nums[1] > nums[0]:
        idx = binary_search_asc(nums, 0, len(nums) - 1, target)
        print(idx)
        exit()

    else:
        idx = binary_search_desc(nums, 0, len(nums) - 1, target)
        print(idx)
        exit()


if __name__ == '__main__':
    main()

