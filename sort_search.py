# Arawela Lou G. Delmo
# This program showcases different sorting and searching algorithms
import time


# ==================== LINEAR SEARCH ====================
def linear_search(my_list: list, target):
    '''
    # NOTE: Linear search works on sorted and unsorted lists
    # NOTE: O(n) runtime; effective for small lists and unsorted lists
    '''
    for i in range(len(my_list)):
        if target == my_list[i]:
            return i
    return None


# ==================== BINARY SEARCH ====================
def binary_search(my_list: list, target):
    '''
    # NOTE: Binary search only works on sorted lists
    # NOTE: O(log(n)) runtime; effective for large lists
    '''
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        guess = my_list[mid]
        # we found our target
        if guess == target: return mid 
        # our target is on the lower half
        elif target < guess: high = mid - 1
         # our target is on the upper half
        elif target > guess: low = mid + 1

    # target not on the list
    return None


# ==================== SELECTION SORT ====================
def selection_sort(mylist: list, order_type: str) -> list:
    '''
    # NOTE: O(n^2) runtime; not that fast
    # NOTE: keep finding the smallest/largest on the UNSORTED part, and swap it with the furthest SORTED part
    '''
    
    arr = mylist.copy()
    
    if order_type == "asc":
        # sort in ascending
        for i in range(len(arr)):
            min = i
            # select the smallest number in the UNSORTED part
            for j in range(i+1, len(arr)):
                # NOTE: here is the main difference between asc and desc
                if arr[j] < arr[min]:
                    min = j
            # swap (put min in correct order)    
            temp = arr[i]
            arr[i] = arr[min]
            arr[min] = temp
    elif order_type == "desc":
        # sort in descending
        for i in range(len(arr)):
            max = i
            # select the largest number in the UNSORTED part
            for j in range(i+1, len(arr)):
                # NOTE: here is the main difference between asc and desc
                if arr[j] > arr[max]:
                    max = j
            # swap (put max in correct order)    
            temp = arr[i]
            arr[i] = arr[max]
            arr[max] = temp

    return arr


# ==================== BUBBLE SORT ====================
def bubble_sort(mylist: list, order_type: str) -> list:
    '''
    # NOTE: O(n^2) runtime
    # NOTE: bubble up numbers
    # NOTE: keep swapping adjacent pairs if needed, return to the beginning and swap pairs again as needed 
    '''

    arr = mylist.copy()
    
    if order_type == "asc":
        # first loop serves as the iterator (will keep going until i is the last element if no break occurs)
        for i in range(len(arr)):
            swapped = False
            # print(f"i is {i}")

            # second loop checks each adjacent pairs
            # (len(arr)-i-1 : after outer loop iteration, largest element in UNSORTED "bubbles up" to its correct position at the end of the array
            for j in range(0, len(arr)-i-1):
                # print(j, arr)
                if arr[j] > arr[j+1]:
                    # print(f"swapping ... index {j} and {j+1}")
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            # print(f"???? swapped: {swapped}\n")
            if not swapped:
                break
    elif order_type == "desc":
        # first loop serves as the iterator (will keep going until i is the last element if no break occurs)
        for i in range(len(arr)):
            swapped = False

            # second loop checks each adjacent pairs
            # (len(arr)-i-1 : after outer loop iteration, largest element in UNSORTED "bubbles up" to its correct position at the end of the array
            for j in range(0, len(arr)-i-1):
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if not swapped:
                break

    return arr      


# ==================== HEAP SORT ====================
# TODO: further study
def heapify(arr, N, i, heap_type):
    '''
    utility function for Heap Sort
    goal: parent node should be greater than both it's child
    '''
    largest = i     # initialize largest as the root
    # NOTE: children of a node can be computed as such:
    left_child = 2 * i + 1 
    right_child = 2 * i + 2

    if heap_type == "max":
        if (left_child < N) and (arr[left_child] > arr[largest]):
            largest = left_child
        if (right_child < N) and (arr[right_child] > arr[largest]):
            largest = right_child

        # perform swap if a child is bigger than parent
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            # fix the affected subtree
            heapify(arr, N, largest, "max")
    if heap_type == "min":
        if (left_child < N) and (arr[left_child] < arr[largest]):
            largest = left_child
        if (right_child < N) and (arr[right_child] < arr[largest]):
            largest = right_child

        # perform swap if a child is smaller than parent
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            # fix the affected subtree
            heapify(arr, N, largest, "min")
    

def heap_sort(mylist: list, order_type: str) -> list:
    '''
    # Heap sort builds a complete binary tree, then transform into max/min heap
    # NOTE: O(log(n)) time complexity
    '''

    arr = mylist.copy()
    
    heap_type = "max" if order_type == "asc" else "min"

    # build complete binary tree    
    # transform into max heap (parent should always be greater than or equal to the child nodes)
        # len(arr) // 2 - 1 ---- this is the furthest parent node
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, len(arr), i, heap_type)


    # perform heap sort (extract elements one by one)
    for i in range(len(arr)-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the root (max element) with the last element
        heapify(arr, i, 0, heap_type)  # Heapify the reduced heap

    return arr


# ==================== MERGE SORT ====================
def merge_sort(mylist: list, order_type: str) -> list:
    '''
    # NOTE: O(nlog(n)) time complexity
    # NOTE: divide and conquer
    # NOTE: split the list into two, sort each half, then merge them back together
    # NOTE: it is necessary that the two halves are sorted 
    # NOTE: pointers: i->left_half, j->right_half, k->arr
    # NOTE: (on asc) when i < j, put i in arr, else put j in arr (k is always incremented)
    # NOTE: when one half is exhausted, put the remaining elements of the other half in arr
    '''
    arr = mylist.copy()

    if len(arr) > 1:
        mid = len(arr) // 2

        # split the list into two
        left_half = arr[:mid]
        right_half = arr[mid:]

        # sort each half
        merge_sort(left_half, order_type)
        merge_sort(right_half, order_type)


        i = j = k = 0
        while (i < len(left_half)) and (j < len(right_half)):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # check if there are any remaining elements in either half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    
    return arr
















def main(): 
    NUM = 10000000
    sortedList = []
    for i in range(NUM):
        sortedList.append(i)


    # linear search
    start_time = time.time()
    result = linear_search(sortedList, 100000)
    end_time = time.time()
    runtime = end_time - start_time
    print(f"Linear Search: target found in index {result}\nruntime: {runtime}\n")
    
    # binary search
    start_time = time.time()
    result = binary_search(sortedList, 100000)
    end_time = time.time()
    runtime = end_time - start_time
    print(f"Binary Search: target found in index {result}\nruntime: {runtime}\n")

    # selection sort
    unsortedList = [2,4,1,5,3]
    result = selection_sort(unsortedList, "asc")
    print(f"Selection Sort: list {unsortedList} sorted...\nnew list: {result}\n")
    
    # bubble sort
    unsortedList = [2,4,1,5,3]
    result = bubble_sort(unsortedList, "asc")
    print(f"Bubble Sort: list {unsortedList} sorted...\nnew list: {result}\n")
    
    # heap sort
    unsortedList = [2,4,1,5,3]
    result = heap_sort(unsortedList, "asc")
    print(f"Heap Sort: list {unsortedList} sorted...\nnew list: {result}\n")

    # merge sort
    unsortedList = [2,4,1,5,3]
    result = merge_sort(unsortedList, "asc")
    print(f"Merge Sort: list {unsortedList} sorted...\nnew list: {result}\n")

if __name__ == '__main__':
    main()

