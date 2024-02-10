#include <stddef.h>
#include <stdio.h>

void quickSortRecurse(int *list, int lowIndex, int highIndex) {
  if (lowIndex >= highIndex) {
    return;
  }

  int finalPivotIndex = lowIndex;
  int pivot = list[highIndex];

  for (int i = lowIndex; i < highIndex; i++) {
    if (list[i] < pivot) {
      int temp = list[finalPivotIndex];
      list[finalPivotIndex] = list[i];
      list[i] = temp;
      finalPivotIndex++;
    }
  }

  int temp = list[finalPivotIndex];
  list[finalPivotIndex] = pivot;
  list[highIndex] = temp;

  quickSortRecurse(list, lowIndex, finalPivotIndex - 1);
  quickSortRecurse(list, finalPivotIndex + 1, highIndex);
}

void quickSort(int *list, size_t listSize) {
  int lowIndex = 0;
  int highIndex = listSize - 1;

  quickSortRecurse(list, lowIndex, highIndex);
}

int main() {
  int list[5] = {3, 1, 5, 2, 4};
  printf("Input: ");
  for (int i = 0; i < 5; i++) {
    printf("%d", list[i]);
  }

  quickSort(list, 5);

  printf("\nOutput: ");
  for (int i = 0; i < 5; i++) {
    printf("%d", list[i]);
  }
}
