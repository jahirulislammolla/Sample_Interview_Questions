# Interview-Practice
Sample Interview Questions - Set 1
Duration: 1 Hour

    What is the output of following code?

#include<cslib>
#define C 9+1
int main()
{
	printf("%d\n",C*C);
	return 0;
}

    Reverse order of dot-delimited elements in a string.

Input: i.love.you.so.much
Output: much.so.you.love.i

    Count ways to reach the n’th stair: Leetcode problem

    There are n stairs, a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs at a time. Count the number of ways, the person can reach the top.

Input: n = 1
Output: 1
There is only one way to climb 1 stair

Input: n = 2
Output: 2
There are two ways: (1, 1) and (2)

Input: n = 4
Output: 5
(1, 1, 1, 1), (1, 1, 2), (2, 1, 1), (1, 2, 1), (2, 2)

    Maximum AND: Hackerearth Problem

    Given two numbers A and B. Find the value of pair (P,Q) such that A <= P < Q <= B value of P AND Q is maximum where AND is a binary operator. Refer to this link for more information about AND operator : http://en.wikipedia.org/wiki/Bitwise_operation#AND

    Input:
    First line of input contains number of test cases T. Each test case contains two numbers A and B.

    Output: For each test case print the value of maximum AND.

    Constraints:
    1<=T<=1000
    1<= A < B <=1018

Sample Input:
2
2 3
4 8

Sample Output:
2
6

    Swap Case: Hackerrank Problem
    You are given a string S. Your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
    For Example:

    HackerRank ? hACKERrANK
    Pythonist 2 ? pYTHONIST 2

    Same Tree: Leetcode Problem
    Given two binary trees, write a function to check if they are equal or not. Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

    Search Insert Position: Leetcode Problem
    Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 -> 2
[1,3,5,6], 2 -> 1
[1,3,5,6], 7 -> 4
[1,3,5,6], 0 -> 0
