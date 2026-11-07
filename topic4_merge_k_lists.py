"""Тема 4. Злиття k відсортованих списків (на основі merge sort, divide and conquer)."""


def merge_two(left: list[int], right: list[int]) -> list[int]:
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def merge_k_lists(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []
    if len(lists) == 1:
        return lists[0]
    mid = len(lists) // 2
    return merge_two(merge_k_lists(lists[:mid]), merge_k_lists(lists[mid:]))


if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)
