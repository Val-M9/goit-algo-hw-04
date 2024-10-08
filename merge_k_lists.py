def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_k_lists(lists):
    if not lists:
        return []

    while len(lists) > 1:
        merged_lists = []
        for i in range(0, len(lists), 2):
            left = lists[i]
            right = lists[i + 1] if i + 1 < len(lists) else []
            merged_lists.append(merge(left, right))
        lists = merged_lists

    return lists[0]


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
