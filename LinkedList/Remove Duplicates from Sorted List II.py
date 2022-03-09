  def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy =ListNode(0) #dummy node which connects to head of the given linkedlist
        dummy.next=head
        prev=dummy     #we are pointing with the prev to the linkedlist
        while head :  #till the end of the linked list
            if head.next and head.val==head.next.val: # we are checking the element if head next element is present and head.val and head.next.val are same or not
                while head.next and head.val ==head.next.val:# keep iterating until we didn't get ay different element
                    head=head.next    #keep traversing 
                prev.next=head.next # if we get then make a connection 
            else:
                prev= prev.next #otherwise not getting the equal element so keep move the prev and head pointer
                
            head=head.next
        return dummy.next
      
      #Try out here- https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
        
