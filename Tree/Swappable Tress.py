Given two trees root0 and root1, return whether you can transform root0 into root1 by swapping any node's left and right subtrees any number of times.
input=root0 = [1, [3, null, null], [4, [0, null, [2, null, null]], null]]
root1 = [1, [3, null, null], [4, [0, null, [2, null, null]], null]]

o/p= True

link= https://binarysearch.com/problems/Swappable-Trees


class Solution:
    
    def solve(self, root0, root1):
        if root0==None and root1==None:
            return True
        
        if root0==None:
            return False
        if root1==None:
            return False
        
        
        if root0!=None and root1!=None:
            if root0.val!=root1.val:
                return False

        return (self.solve(root0.left,root1.left) and self.solve(root0.right,root1.right))  or (self.solve(root0.left,root1.right) and self.solve(root0.right,root1.left)) 
