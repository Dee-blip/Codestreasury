# Maximum Subarray Sum
# This problem was asked by Amazon.
# Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
# For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.
# Given the array [-5, -1, -8, -9], the maximum sum would be -1.
# Follow up: Do this in O(N) time.


n=int(input())
arr=list(map(int,input().split()))

for i in range(1,n):
    if arr[i-1]>0:
        arr[i]=arr[i]+arr[i-1]
        
    else:
        arr[i-1]=0
        
print(max(arr))
