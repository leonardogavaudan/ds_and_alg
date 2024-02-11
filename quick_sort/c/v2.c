#include <stddef.h>
#include <stdio.h>

void quickSortRecurse(int *list, int lowIndex, int highIndex) {
  if (lowIndex >= highIndex) {
    return;
  }

  int pivotIndex = lowIndex;
  int pivot = list[highIndex];

  for (int i = lowIndex; i < highIndex; i++) {
    if (list[i] < pivot) {
      int temp = list[i];
      list[i] = list[pivotIndex];
      list[pivotIndex] = temp;
      pivotIndex++;
    }
  }

  list[highIndex] = list[pivotIndex];
  list[pivotIndex] = pivot;

  quickSortRecurse(list, lowIndex, pivotIndex - 1);
  quickSortRecurse(list, pivotIndex + 1, highIndex);
}

void quickSort(int *list, size_t listSize) {
  quickSortRecurse(list, 0, listSize - 1);
}

int main() {
  int list[] = {10, 7, 8, 9, 1, 5};
  size_t n = sizeof(list) / sizeof(list[0]);

  quickSort(list, n);

  printf("Sorted array: \n");
  for (size_t i = 0; i < n; i++) {
    printf("%d ", list[i]);
  }
  printf("\n");

  return 0;
}
