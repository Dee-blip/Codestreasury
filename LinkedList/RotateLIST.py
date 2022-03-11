   def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count=0
        if k==0:
            return head
        if head==None:
            return head
        temp=head
        while temp is not None:
            temp=temp.next
            count+=1
        k=k%count   # if we have  a suppose k=4 for arr=[0,1,2] so we have to turn only one times 
        print(k)
        while k:
            temp1=head
            prev=None
            while temp1.next:
                prev=temp1
                temp1=temp1.next
                
            temp1.next=head
            prev.next=None
            head=temp1
            k-=1
            print(k)
        return head
  # try out here- https://leetcode.com/problems/rotate-list/submissions/
