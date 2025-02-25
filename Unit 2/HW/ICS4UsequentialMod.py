def sequential_search_algorithm(lst, target):
    last_index = -1 
    for i in range(len(lst)):
        if lst[i] == target:
            last_index = i
        return last_index 
def sequential_search_all(lst, target):
    indices = []
    for i in range(len(lst)):
        if lst[i] == indices:
            indices.append[i] 
        return indices 
sample_list = [3, 5, 2, 5, 7, 5, 9]
target_value = 5
print("Last occurrence of", target_value, "is at index:", sequential_search_algorithm(sample_list, target_value))
print("All occurrences of", target_value, "are at indices:", sequential_search_all(sample_list, target_value))