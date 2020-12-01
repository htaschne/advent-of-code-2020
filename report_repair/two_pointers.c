#include <stdio.h>
#include <stdlib.h>

int comp(const void * a, const void * b) {
  return ( *(int*)a - *(int*)b );
}

int main() {
  int n; scanf("%d", &n);
  int *vet = (int*) malloc(sizeof(int) * n);

  int num;
  for (int i = 0; scanf("%d", &num) == 1; ++i) {
    vet[i] = num;
  }

  qsort(vet, n, sizeof(int), comp);

  int left = 0, right = n - 1;
  while (left <= right) {
    int sum = vet[left] + vet[right];

    if (sum == 2020) {
      int a = vet[left];
      int b = vet[right];
      printf("%d * %d = %d\n", a, b, a * b);
      return 0;
    } else if (sum < 2020) {
      left++;
    } else if (sum > 2020) {
      right--;
    } 
  }

  return -1;
}
