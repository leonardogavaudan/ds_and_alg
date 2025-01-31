#include <stdio.h>

void selectionSort(int *list, int length) {
  for (int i = 0; i < length - 1; i++) {
    int minIndex = i;
    for (int k = i + 1; k < length; k++) {
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
  int list[] = {3, 2, 5, 4, 1};
  selectionSort(list, 5);

  for (int i = 0; i < 5; i++) {
    printf("%d ", list[i]);
  }

  return 0;
}
