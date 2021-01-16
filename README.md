# Efficient-Closest-Pair-of-Points

>`Purpose:` Course assignment at [IIITD](https://www.iiitd.ac.in/)

>[`Instructions:`](/instruction.pdf) (Credits- [Introduction to Programming](http://techtree.iiitd.edu.in/viewDescription/filename?=CSE101))

>`Details:`
The native brute-force method to find minimum distance between two points in the set of n points takes (n^2) computations. The plan is to avoid polynomial time complexity to calculalte the closest pair.
The idea is to use the infamous Divide and Conquer method to do better than intutive brute-force.
Modified Time complexity to find closest pair- O(nlog^2(n)), which is a major boost to the simple brute-force.