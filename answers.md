# CMPS 2200 Assignment 4
## Answers

**Name:**___Amara Midouhas______________________


Place all written answers from `assignment-04.md` here for easier grading.

**1a)** An example would be starting with the largest denomination so 2^k. Then keep subtracting 2^k from N and keep grabbing the largest denomination and subtracting from N  until you get 0. 

**1b)** The greedy choice is to pick the largest denomination and that this will lead to an optimal soltuion. To show this is optimal, we will have to ensure that all the solutions from subtrating the largest denomination , k, from n in the substructure is also optimal. 

**1c)** The work is O(log N) because it is proportional to the amount of iteration it takes for n=0 . For span, each step is independent of each other as it matters how many iterations it takes to reduc N to 0 so also O(Log N )

**1d)** An counterexample would be:
D1 = 4
D2 = 6 
N = 8

The Greedy Algorithm would choose 6 , so then n=2. Next it would choose 4, so then n =2, so now there are 2 coins for D1 whixh is less then the greedy algorithim 

**1e)** There exist an optimal solution to change the amount remaining after subratcting denominuation Di from total amount N (N-Di).
Proof: Lets represent the optimal solution as O(N) for making changes amount for N then O(N-Di), will be an optimal solution for making change sto the remaining amount N-Di. If there is a better solution then we can combine it with Di to get a better solution for O(N).

**1f)** I would use a bottom up structure. We would create an memoization array with size of N+1 to store the minimum number of coins to make a change for each amount from 0 to N. So  array[0]=0 , then For each amount i from 1 to N, calculate array[i]. So something like this array[i] = min(Dj ≤ i) { dp[i - Dj] + 1 }, where Dj is one of the available denominations.

The work is proportional to the number of subproblems, which is O(N * k), where k is the number of denominations. The span is determined by the max depth of the recursion, which is O(log N).