#include <stdio.h>

int main() {
  int prev, new, counter;

  counter = 0;

  /* Manually read the first element */
  scanf("%d\n", &prev);

  /* Loop-read the rest of the elements */
  while (scanf("%d\n", &new) != EOF) {
    if (new > prev) counter++;
    prev = new;
  }
  printf("First star: %d\n", counter);
}
