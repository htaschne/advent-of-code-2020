#!/usr/bin/env bash

echo -e "part one: "
gcc -O3 two_pointers.c -o two_pointers && ./two_pointers < 0.in

echo -e "part two: "
gcc -O3 horse.c -o horse && ./horse < 0.in

# clean
rm two_pointers
rm horse
