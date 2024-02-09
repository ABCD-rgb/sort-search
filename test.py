import sort_search as ss
import random


N = 20
arr = []
for i in range(N):
    random_num = int(random.random() * N)
    # ensure no duplicates
    while random_num in arr:
        random_num = int(random.random() * N)
    arr.append(random_num)


bubble = ss.bubble_sort(arr, "asc")
print(f"BUBBLE SORT: {bubble}")
selection = ss.selection_sort(arr, "desc")
print(f"SELECTION SORT: {selection}")





def merge_sort(mylist: list, order_type: str) -> list:
    '''
    # NOTE: O(nlog(n)) time complexity
    # NOTE: divide and conquer
    # NOTE: split the list into two, sort each half, then merge them back together
    '''

    arr = mylist.copy()

    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # sort each half
        merge_sort(left_half, order_type)
        merge_sort(right_half, order_type)

        # merge the two halves
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
