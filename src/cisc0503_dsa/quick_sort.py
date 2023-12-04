import sys
IS_IDLE = "idlelib" in sys.modules

def quickSort(arr, simple=False, verbose=False):
    """
    The main function to sort an array using QuickSort algorithm.
    Optionally uses a simple partitioning scheme.
    """
    if simple:
        partition_fn = partitionSimple
    else:
        partition_fn = partition

    _quickSort(arr, 0, len(arr) - 1, partition_fn, verbose)
    return arr

def _quickSort(arr, low, high, partition_fn, verbose):
    """
    The recursive function that implements the QuickSort algorithm.
    """
    if low < high:
        # Find the partitioning index
        pivot_index = partition_fn(arr, low, high, verbose)

        # Separately sort elements before and after partition
        _quickSort(arr, low, pivot_index - 1, partition_fn, verbose)
        _quickSort(arr, pivot_index + 1, high, partition_fn, verbose)

def medianOfThree(arr, low, high):
    """
    Helper function to find the median of three values in the array.
    The values are the first, middle, and last element of the array segment.
    """
    mid = (low + high) // 2
    # Sort these elements using simple comparison
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    # Now, the median is at the middle position
    return mid

def partition(arr, low, high, verbose=False):
    """
    This function selects the median of the first, middle, and last elements as the pivot.
    It then places the pivot element at its correct position in the sorted array, and
    positions all smaller elements to the left of the pivot and all greater elements to the right.
    """
    # Get the index of the median of three
    median_index = medianOfThree(arr, low, high)
    if verbose:
        n = max(len(str(x)) for x in arr)
        prefix = f" sorting from index {low:>{n}} to {high:>{n}}, pivot @ {median_index:>{n}}"
        print(f"{prefix}: {formatDisplay(arr, low, high, median_index, n)}")
    # Swap median with high to use it as pivot
    arr[median_index], arr[high] = arr[high], arr[median_index]

    pivot = arr[high]  # pivot
    i = low - 1       # Index of smaller element

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot element with the element at i+1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def partitionSimple(arr, low, high, verbose=False):
    """
    This function takes the first element as pivot, places the pivot element at its
    correct position in sorted array, and places all smaller to left of pivot and
    all greater elements to right of pivot.
    """
    pivot = arr[low]  # pivot
    i = low + 1       # Index of smaller element

    if verbose:
        n = max(len(str(x)) for x in arr)
        prefix = f" sorting from index {low:>{n}} to {high:>{n}}, pivot @ {low:>{n}}"
        print(f"{prefix}: {formatDisplay(arr, low, high, low, n)}")

    for j in range(low + 1, high + 1):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # Swap the pivot element with the element at i-1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

def formatDisplay(arr, low, high, pivotIndex, n):
    list_display = ""
    pivot = False
    if not IS_IDLE:
        for i in range(len(arr)):
            if i >= low and i <= high:
                # green
                color = f"\033[32m"
            else:
                # no color
                color = f"\033[0m"
            pivot = i == pivotIndex
            element = arr[i]
            if pivot:
                element = f"⟨{element:>{n}}⟩"
            else:
                element = f" {element:>{n}} "
            display = f"{color}{element}"
            display += "\033[0m"
            list_display += display
    else: # pragma: no cover
        # IDLE doesn't support colors, so instead we'll bracket the part
        # of the array that is being sorted with [ and ], and also bracket the part that
        # isn't being sorted with ( and ).
        size = len(arr)
        for i in range(size):
            prefix, suffix = "", ""
            if i == low:
                prefix = "["
            else:
                prefix = " "
            if i == high:
                suffix = "]"
            else:
                suffix = " "
            if i == high+1:
                prefix = " " # (
            if i == size-1 and i != high:
                suffix = " " # )
            pivot = i == pivotIndex
            element = arr[i]
            if pivot:
                display = f"{prefix}⟨{element:>{n}}⟩{suffix}"
            else:
                display = f"{prefix} {element:>{n}} {suffix}"
            list_display += f"{display}"

    return list_display

def quickSortIterative(arr, simple=False, verbose=False):
    # Choose the partition function based on the 'simple' flag
    fn = partitionSimple if simple else partition

    # Stack for storing the start and end indices of the sub-arrays
    size = len(arr)
    stack = [(0, size - 1)]

    # Process each sub-array from the stack
    while stack:
        start, end = stack.pop()
        if start < end:
            pivotIndex = fn(arr, start, end, verbose)

            # Push sub-arrays to the stack
            stack.append((start, pivotIndex - 1))
            stack.append((pivotIndex + 1, end))

    return arr
