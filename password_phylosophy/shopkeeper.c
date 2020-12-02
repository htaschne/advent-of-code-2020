#include <stdio.h>

int main() {
  int lo, hi, valid = 0;
  char letter, buff[256];
  while (scanf("%d-%d %c: %s", &lo, &hi, &letter, buff) == 4)
    if ((buff[lo - 1] == letter) ^ (buff[hi - 1] == letter))
      valid++;
  printf("%d\n", valid);
}
