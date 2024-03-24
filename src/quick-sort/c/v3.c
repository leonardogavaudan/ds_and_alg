#include <stddef.h>
#include <stdio.h>

void quickSortRecurse(int *list, int lowIndex, int highIndex) {
  if (lowIndex >= highIndex) {
    return;
  }

  int pivot = list[highIndex - 1];
  int pivotIndex = lowIndex;

  for (int i = lowIndex; i < highIndex; i++) {
    if (list[i] < pivot) {
      int temp = list[pivotIndex];
      list[pivotIndex] = list[i];
      list[i] = temp;
      pivotIndex++;
    }
  }

  list[highIndex - 1] = list[pivotIndex];
  list[pivotIndex] = pivot;

  quickSortRecurse(list, lowIndex, pivotIndex - 1);
  quickSortRecurse(list, pivotIndex + 1, highIndex);
}

void quickSort(int *list, size_t listSize) {
  quickSortRecurse(list, 0, listSize);
}

int main() {
  int list[] = {9, 7, 5, 11, 12, 2, 14, 3, 10, 6};
  size_t listSize = sizeof(list) / sizeof(list[0]);

  printf("Original array:\n");
  for (size_t i = 0; i < listSize; i++) {
    printf("%d ", list[i]);
  }
  printf("\n");

  quickSort(list, listSize);

  printf("Sorted array:\n");
  for (size_t i = 0; i < listSize; i++) {
    printf("%d ", list[i]);
  }
  printf("\n");

  return 0;
}
