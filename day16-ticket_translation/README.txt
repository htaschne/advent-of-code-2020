so today's part 2 was a bit messy...
part 1 star is the first thing scanner.py prints. after that it prints all the ticket spaces and the rules that space can't match.

for example, the following
  space 5 ( 106 ) can't match rule 15

  ... means that the space 5 in the ticket can't be matched by the rule 15.

so after that I ran sorter.py, which does the opposite. meaning that given a set of rules a space can't match it prints the only rules it can match! and the result of that is saved in the can_table.txt file.

so in short the can_table.txt will have a ticket space and the rules it can match.
and it's like a set of equations where one ticket space will have only a single rule, and another two rules, etc...
and if you keep deleting the rules from each space list that are already matched by another space every space will only match a single rule.

for example:

  12 [9]
  6  [9, 17]
  0  [9, 16, 17]

in this example since space 12 can only be matched by rule 9 then space 6 obviously will only match rule 17 and space 0 will only match rule 16.

using this logic I solved part 2 and the notes are on table.txt.

maybe will comeback and refactor this in a single python script. or not. I had a lot of fun either way!
