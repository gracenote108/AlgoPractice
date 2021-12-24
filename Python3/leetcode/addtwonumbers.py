# Definition for singly-linked list.


class LinkedList:

    def __init__(self, prList=None):
        self.root = None
        if prList != None:
            for x in prList:
                self.add(x)

    def add(self, value):
        if self.root == None:
            self.root = ListNode(value)
        else:
            current = self.root
            while current.next != None:
                current = current.next
            current.next = ListNode(value)

    def getRoot(self):
        return self.root


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        throwNode = ListNode()
        current = throwNode
        carry = 0
        sum = 0
        while l1 != None or l2 != None or carry > 0:
            sum += carry
            carry = 0

            if l1 != None:
                sum += l1.val
                l1 = l1.next

            if l2 != None:
                sum += l2.val
                l2 = l2.next

            if sum > 9:
                carry = int(sum/10)
                sum = sum % 10

            current.next = ListNode(sum)
            current = current.next
            sum = 0
        return throwNode.next


list1 = [2, 4, 3]
list2 = [5, 6, 4]

l1 = LinkedList(list1).getRoot()
l2 = LinkedList(list2).getRoot()

sol = Solution()

result = sol.addTwoNumbers(l1, l2)

output = []

while result != None:
    output.append(result.val)
    result = result.next
output.reverse()
print(output)
