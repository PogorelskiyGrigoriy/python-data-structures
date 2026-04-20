def binary_search(sorted_list:list, search_key) -> int:
    """
    return the index of the search_key in the sorted_list
    return -(insort_index + 1) if search_key is not found
    """
    low = 0
    high = len(sorted_list) - 1
    

    while low <= high:
        mid = (low + high) // 2
        mid_val = sorted_list[mid]

        if mid_val < search_key:
            low = mid + 1
        elif mid_val > search_key:
            high = mid - 1
        else:
            res=mid

    return res if res else -(low + 1)

def insort(sorted_list:list, item) -> list: 
    """Insert item in sorted_list, and keep it sorted assuming sorted_list is sorted."""
    low = 0
    high = len(sorted_list)

    while low < high:
        mid = (low + high) // 2
        if sorted_list[mid] < item:
            low = mid + 1
        else:
            high = mid

    sorted_list.insert(low, item)
    return sorted_list
