'''You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given the integer array fruits, return the maximum number of fruits you can pick.'''

class Solution:
    '''
    Runtime: 696 ms, faster than 91.58% of Python3 online submissions for Fruit Into Baskets.
    Memory Usage: 20.2 MB, less than 33.12% of Python3 online submissions for Fruit Into Baskets.

    Time: O(n)
    Space: O(1)
    '''
    def totalFruit(self, trees: list[int]) -> int:
        baskets = {}
        maxTrees = 0
        start = 0

        for end in range(len(trees)):
            eFruit = trees[end]
            if baskets.get(eFruit):
                maxTrees = max(maxTrees, end - start+1)
            elif not baskets.get(eFruit) and len(baskets) < 2:                
                baskets[eFruit] = True
                maxTrees = max(maxTrees, end - start+1)
            else:
                baskets = {}
                start = end - 1
                while trees[start] == trees[start-1]:
                    start -= 1
                baskets[eFruit] = True
                baskets[trees[start]] = True
        return maxTrees

sol = Solution()
print(sol.totalFruit([1,2,1])) #3
print(sol.totalFruit([0,1,2,2])) #3
print(sol.totalFruit([1,2,3,2,2])) #4
print(sol.totalFruit([3,3,3,1,2,1,1,2,3,3,4])) #5
print(sol.totalFruit([1,0,3,4,3])) #3