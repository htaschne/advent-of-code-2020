#include <stdio.h>
#include <stdlib.h>

int main() {
  int num, n;
  scanf("%d", &n);
  int *v = (int*) malloc(sizeof(int) * n);
  for (int i = 0; scanf("%d", &num) == 1; i++) {
    v[i] = num;
  }

  // why not right?
  for (int i = 0; i < n; i++)
    for (int j = i+1; j < n; j++)
      for (int k = j+1; k < n; k++)
        if (v[i] + v[j] + v[k] == 2020 && i != j && j != k && i != k) {
          int mult = v[i] * v[j] * v[k];
          printf("%d + %d + %d = 2020. %d * %d * %d = %d\n",
              v[i], v[j], v[k], v[i], v[j], v[k], mult);
          return 0;
        }

  return -1;
}
