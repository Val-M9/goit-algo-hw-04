import timeit
import random

numbers = [random.randint(1, 100000) for _ in range(5000)]


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


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


insert_time = timeit.timeit(lambda: insertion_sort(numbers.copy()), number=10)
merge_time = timeit.timeit(lambda: merge_sort(numbers.copy()), number=10)
built_in_time = timeit.timeit(lambda: sorted(numbers.copy()), number=10)
print(f"insert time: {insert_time}")
print(f"merge time: {merge_time}")
print(f"built in time: {built_in_time}")

# Різниця в часі між вбудованим методом сортування та власними методами величезна. Вона помітна навіть
# в порівннянні з часом сортування злиттям, не кажучи вже про час сортування вставками.
# Також варто зазначити, що час сортування злиттям значно менший за час сортування вставками.
# І на великих масивах даних різниця лише зростає. До прикладу проводив тестування на масиві
# 10 000, сортування вставками вже виконувалолсь 23.56 секунди, а злиттям 0.26 секунди, вбудований метод 0.011 сек.
