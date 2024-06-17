from typing import List


def selection_sort(list: List[int]) -> None:
    for i in range(len(list) - 1):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[min_index] > list[j]:
                min_index = j

        list[min_index], list[i] = list[i], list[min_index]


if __name__ == "__main__":
    list = [4, 7, 3, 9, 2]
    selection_sort(list)
    print(list)
