# Script

## 1. What is a permutation? (+ notation)

Before we talk about permutation *groups*, it would be wise to define what a permutation is, as well as some common notation used.

Formally, a permutation is a bijective mapping from a set to itself.

We can write out all permutations for the set {1, 2, 3}-- then putting the permuted row below the original, we now have **array notation** for any permutation.

Given two permutations *sigma* and *gamma*, we can compose them by following the bottom row of the rightmost array through the topmost row of the array to the left.

But what other notation can we use? For some permutation *alpha*, we observe that some elements map to themselves under repeated applications of *alpha*. We can partition the elements of *alpha* into cycles according to this principle. Cycles are not only an interesting property of permutations; they also serve as an alternative notation.

Permutation *groups* are therefore a set of permutations equipped with the permutation composition operation.