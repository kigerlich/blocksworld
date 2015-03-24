# blocksworld

In this problem you must parse a series of commands that instruct a robotic arm to manipulate blocks that lie on a flat table.
Initially there are always "n" blocks on the table, laid flat and numbered from 0 to n-1.

The commands for the robotic arm take this form:
Move a ONTO b

Where a and b are block numbers. This puts block a onto block b after "clearing" any blocks that are stacked on top of blocks a and b to their initial positions. 

Any command in which a = b or in which a and b are in the same stack of blocks is an illegal command. All illegal commands should be ignored and should have no effect on the configuration of blocks. You may also ignore the scenario in which a block that needs to be cleared to its initial position would get in the way of either the source or the target.

Run this example sequence of commands for a blocksworld of size 10 (n = 10).
 move 1 onto 2
 move 5 onto 1
 move 9 onto 5
 move 8 onto 9
 move 6 onto 1
 move 2 onto 4

 Print some representation of the world at the end. 