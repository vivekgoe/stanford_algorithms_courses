# Programming Problem Descriptions
## Problem-1
The goal of this problem is to implement the "Median Maintenance" algorithm. The text file contains a list of the integers from 1 to 10000 in unsorted order; you should treat this as a stream of numbers, arriving one by one. Letting xi denote the ith number of the file, the kth median mk is defined as the median of the numbers x1,…,xk. (So, if k is odd, then mk is ((k+1)/2)th smallest number among x1,…,xk; if k is even, then mk is the (k/2)th smallest number among x1,…,xk.)
Find the sum of the 10000 medians modulo 10000. Use a heap to solve the problem.
## Problem-2
Same problem statement as (1), but use a balanced binary search tree (AVL tree) to solve the problem.
