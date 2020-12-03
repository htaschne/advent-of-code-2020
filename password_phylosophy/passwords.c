#include <stdio.h>

int main() {
  int lo, hi, times, valid = 0;
  char letter, buff[256];
  while (scanf("%d-%d %c: %s", &lo, &hi, &letter, buff) == 4) {
    times = 0;
    for (int i = 0; buff[i] != '\0'; ++i)
      if (buff[i] == letter)
        times++;
    if (times >= lo && times <= hi)
      valid++;
  }
  printf("%d\n", valid);
}
