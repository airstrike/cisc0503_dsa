try:
    from .quick_sort import *
except ImportError:
    from quick_sort import *

import sys
sys.setrecursionlimit(150000)  # Increase the recursion limit

# Assignment 06
# ¯¯¯¯¯¯¯¯¯¯¯¯¯
# In class we learned the pivot used for Quick sort is the first element of the
# array. But we discussed the problem with this approach when the array is already
# sorted. Another method used is take the first value, last value and the middle
# index value of the array and pivot is chosen each time as the value in the
# middle. For example if an array is given as [ 9, 7, 3, 1, 2, 8, 4, 6, 5]. We
# compare 9, 5 and 2 (first value in the array, last value in the array and value
# corresponding to the middle index.) and pick 5 which comes between 2 and 9.
# This is called the Median of Three rule.
#
# a)  Write the status of the list F= (12,2,16, 30,8,28,4,10,20,6,18) at the end of
#     each phase of recursive Quick sort using median of three rule to determine the
#     pivot key. (15 points)
# b)  Write a non recursive version of Quicksort incorporating the median of three
#     rule to determine the pivot key. You can use the F array above from a) for your
#     testing. (25 points)
# c)  Show that QuickSort takes O(n2) time when input list is already in sorted
#     order when we use pivot as the first element in the array. (10 points)
# d)  Show that the non recursive version of Quicksort above takes O( n logn) time
#     on already sorted list when using the Median of three rule. (10 points)
#
# c) and d) in the program can illustrated using a program running time for a big
# array OR using simple illustration in a docx file whichever way is easier for
# you.

def question_a():
    print("\nQuestion A: Write the status of the list F at each phase using the median of three")
    print("            rule to determine the ⟨pivot⟩ index. We'll denote the (sub-)list being sorted with [brackets]")
    print("--------------------------------------------------------------------------------------")
    F = [12, 2, 16, 30, 8, 28, 4, 10, 20, 6, 18]
    quickSort(F, simple=False, verbose=True)

def question_b():
    print("\nQuestion B: Write a non-recursive version of QuickSort using the median of three.")
    print("            We will also print out every stage for comparison purposes")
    print("--------------------------------------------------------------------------------------")
    F = [12, 2, 16, 30, 8, 28, 4, 10, 20, 6, 18]
    quickSortIterative(F, simple=False, verbose=True)


def question_c():
    print("\nQuestion C: Show that QuickSort takes O(n^2) time when the input list is already sorted")
    print("            when using the simple method. In theory, any increase to the size of the")
    print("            list size should correspond to a quadratic increase in the time taken to")
    print("            sort it. We'll demonstrate this by calculating the ratio of the elapsed")
    print("            sorting time relative to the prior pass. As we get to larger, slower lists,")
    print("            the time increase ratio should approach its theoretical value")
    print("--------------------------------------------------------------------------------------")

    import time
    array_sizes = [100, 1000, 10000, 20000, 30000]
    previous_time = None
    previous_size = None
    pad_size = max([len(str(i)) for i in array_sizes])

    for size in array_sizes:
        arr = list(range(size))
        start = time.time()
        quickSort(arr, simple=True, verbose=False)
        end = time.time()
        elapsed_time = end - start

        if previous_time is not None:
            expected_ratio = (size / previous_size) ** 2
            actual_ratio = elapsed_time / previous_time
            print(f"Size: {size:>{pad_size}}, Elapsed: {elapsed_time:>{7}.4f} seconds, Increase: {actual_ratio:>{6}.2f} (vs. theoretical: {expected_ratio:>{6}.2f})")
        else:
            print(f"Size: {size:>{pad_size}}, Elapsed: {elapsed_time:>{7}.4f} seconds")

        previous_time = elapsed_time
        previous_size = size

def question_d():
    print("\nQuestion D: Show that the non-recursive QuickSort with Median of Three rule")
    print("            takes O(n log n) time on already sorted lists.")
    print("            We'll compare the time taken for sorting lists of increasing sizes.")
    print("--------------------------------------------------------------------------------")

    import time
    import math
    array_sizes = [100, 1000, 10000, 100000, 1000000]
    results = []
    pad_size = max([len(str(i)) for i in array_sizes])

    for size in array_sizes:
        arr = list(range(size))
        start = time.time()
        quickSortIterative(arr, simple=False, verbose=False)
        end = time.time()
        elapsed_time = end - start
        results.append((size, elapsed_time))

        if len(results) > 1:
            prev_size, prev_elapsed_time = results[-2]
            actual_ratio = elapsed_time / prev_elapsed_time
            expected_ratio = 10 * (1 + math.log(10) / math.log(prev_size))
            print(f"Size: {size:>{pad_size}}, Elapsed: {elapsed_time:>{7}.4f} seconds, Increase: {actual_ratio:>{6}.2f}",
                  f"(vs. theoretical: {expected_ratio:>{5}.2f})")
        else:
            print(f"Size: {size:>{pad_size}}, Elapsed: {elapsed_time:>{7}.4f} seconds")

def run():
    question_a()
    question_b()
    question_c()
    question_d()
    print("")

if __name__ == '__main__':
    run()
