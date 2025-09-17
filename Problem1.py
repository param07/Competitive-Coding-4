# https://leetcode.com/problems/palindrome-linked-list/

# Method-1: Using Array extra space
# Time Complexity : O(N)
# Space Complexity : O(N)
# Did this code successfully run on GFG : Yes
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach in three sentences only
# Iterating through linkedlist and storing the nodes in an array that is a contiguous memory data structure.
# This helps to check for palindrome using two pointers on the array

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        # method-1
        # using extra space
        curr = head
        arr = []
        while(curr):
            arr.append(curr)
            curr = curr.next

        low = 0
        high = len(arr) - 1
        while(low < high):
            if((arr[low]).val != (arr[high]).val):
                # not a palindrome
                return False
            low += 1
            high -= 1

        # It is a palindrome
        return True
    

print("Method1: Using Array extra space")
node1 = ListNode(1)
node2 = ListNode(2)
node22 = ListNode(2)
node11 = ListNode(1)
head = node1
node1.next = node2
node2.next = node22
node22.next = node11

sol = Solution()

print(sol.isPalindrome(head))

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node22 = ListNode(2)
node11 = ListNode(1)
head = node1
node1.next = node2
node2.next = node3
node3.next = node22
node22.next = node11

print(sol.isPalindrome(head))

node5 = ListNode(5)
node6 = ListNode(6)
node5.next = node6
head = node5

print(sol.isPalindrome(head))


# Method-2: Using reversing second half of linked list and checking palindrome
# Time Complexity : O(N)
# Space Complexity : O(1)
# Did this code successfully run on GFG : Yes
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach in three sentences only
# Here we broke the problem into steps. First we found the middle of linked list using fast and slow pointer. Then we reversed the second
# half of the linked list. We point slow at the end of the original list which is now the front of the reversed second half. We point another
# pointer at the front of the orginal list. Now we can use two pointer on the linkedlist and compare the values.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if(not head.next):
            return True
        slow = head
        fast = head
        # in this both even and odd cases are covered
        # for even number, the slow stops at first mid
        # for odd number, slow stops at mid
        while(fast.next and fast.next.next):
            fast = fast.next.next
            slow = slow.next

        # revese the second half
        prev = slow
        slow = slow.next
        prev.next = None

        while(slow):
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # now lets check palindrome
        slow = prev
        fast = head

        # for even case fast will reach null
        # for odd case slow == fast
        while(fast and slow != fast):
            if(fast.val != slow.val):
                return False

            fast = fast.next
            slow = slow.next

        return True

print("Method2: Using reversing second half of linked list and checking palindrome")
node1 = ListNode(1)
node2 = ListNode(2)
node22 = ListNode(2)
node11 = ListNode(1)
head = node1
node1.next = node2
node2.next = node22
node22.next = node11

sol = Solution()

print(sol.isPalindrome(head))

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node22 = ListNode(2)
node11 = ListNode(1)
head = node1
node1.next = node2
node2.next = node3
node3.next = node22
node22.next = node11

print(sol.isPalindrome(head))

node5 = ListNode(5)
node6 = ListNode(6)
node5.next = node6
head = node5

print(sol.isPalindrome(head))