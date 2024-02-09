#include "stddef.h"
#include <stdio.h>

void selectionSort(int *list, size_t listSize) {
  for (int i = 0; i < listSize; i++) {
    int minIndex = i;

    for (int k = i + 1; k < listSize; k++) {
      if (list[k] < list[minIndex]) {
        minIndex = k;
      }
    }

    int minValueTemp = list[minIndex];
    list[minIndex] = list[i];
    list[i] = minValueTemp;
  }
}

int main() {
  int list[5] = {4, 3, 1, 2, 5};

  printf("Input: ");
  for (int i = 0; i < 5; i++) {
    printf("%d ", list[i]);
  }

  selectionSort(list, 5);

  printf("\nSorted array: ");
  for (int i = 0; i < 5; i++) {
    printf("%d ", list[i]);
  }
}
