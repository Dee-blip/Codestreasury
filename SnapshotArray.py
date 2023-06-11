# https://leetcode.com/problems/snapshot-array/description/
class SnapshotArray:
    
    def __init__(self, length: int):
        self.arr=[[(0,0)] for i in range(length)]
        self.count=0
        
    def set(self, index: int, val: int) -> None:
        self.arr[index].append((self.count,val))
  

    def snap(self) -> int:
        self.count+=1
        return self.count-1

    def get(self, index: int, snap_id: int) -> int:
        snaps=self.arr[index]
        left,right=0,len(snaps)-1
        while left<=right:
            mid=(left+right)//2
            if snaps[mid][0]<=snap_id:
                left=mid+1
            else:
                right=mid-1
        return snaps[right][1]
        
        
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
