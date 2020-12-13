#include <math.h>
#include <stdio.h>

int comp(const void *a, const void *b) {
  int *l = (int *)a;
  int *r = (int *)b;
  return (*l) - (*r);
}

int main() {
  int n;
  scanf("%d", &n);

  int seats[n];
  int it = 0;

  // row
  char line[11];
  int high = 0;
  for (int x = 0; x < n; x++) {
    scanf("%s", line);
    int lo = 0;
    int hi = 127;

    for (int i = 0; i < 7; i++) {
      // printf("%d %d\n", lo, hi);
      if (line[i] == 'F') {
        hi = ceil((hi + lo) / 2.0);
      } else {
        lo = ceil((lo + hi) / 2.0);
      }
    }

    int row = lo;

    // col
    lo = 0;
    hi = 7;
    for (int i = 7; i < 10; ++i) {
      // printf("%d %d\n", lo, hi);
      if (line[i] == 'R') {
        lo = floor((lo + hi) / 2.0);
      } else {
        hi = floor((lo + hi) / 2.0);
      }
    }

    int col = hi;

    // seat
    int seat = row * 8 + col;
    high = seat > high ? seat : high;
    seats[it++] = seat;
  }

  printf("%d\n", high);

  qsort(seats, n, sizeof(int), comp);
  for (int i = 0; i < n - 1; i++) {
    if (seats[i] + 1 != seats[i + 1]) {
      printf("%d\n", seats[i]);
      return 0;
    }
  }

  return -1;
}
