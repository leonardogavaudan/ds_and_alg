#include <stdio.h>

void selectionSort(int *list, int listSize) {
  for (int i = 0; i < listSize; i++) {
    int minIndex = i;
    for (int k = i + 1; k < listSize; k++) {
      if (list[k] < list[minIndex]) {
        minIndex = k;
      }
    }

    int temp = list[i];
    list[i] = list[minIndex];
    list[minIndex] = temp;
  }
}

int main() {
  int list[] = {64, 25, 12, 22, 11};
  int listSize = sizeof(list) / sizeof(list[0]);

  selectionSort(list, listSize);

  printf("Sorted array: \n");
  for (int i = 0; i < listSize; i++) {
    printf("%d ", list[i]);
  }
  printf("\n");

  return 0;
}
