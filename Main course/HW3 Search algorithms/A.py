def print_min_elem_with_min_abs_distance(arr, lenght_of_array, query):
    """Find lower bound"""
    left = 0
    right = lenght_of_array - 1
    while left < right - 1:
        mid = int((left + right) / 2)
        if arr[mid] >= query:
            right = mid
        else:
            left = mid
    if query - arr[left] <= arr[right] - query:
        print(arr[left])
    else:
        print(arr[right])


lenght_of_array, lenght_of_queries = map(int, input().split())
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))

for query in queries:
    print_min_elem_with_min_abs_distance(arr, lenght_of_array, query)