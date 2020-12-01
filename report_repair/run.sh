#!/usr/bin/env bash

echo -e "part one: "
gcc -O3 two_pointers.c -o two_pointers && ./two_pointers < 0.in && rm two_pointers

echo -e "part two: "
gcc -O3 horse.c -o horse && ./horse < 0.in && rm horse
